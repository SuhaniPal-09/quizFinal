from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Option, Question, Quiz, QuizResult, UserProfile


class QuizFlowTests(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(
            username='teacher',
            password='password123',
            is_staff=True,
        )
        self.student = User.objects.create_user(
            username='student',
            password='password123',
        )
        self.other_student = User.objects.create_user(
            username='other-student',
            password='password123',
        )
        UserProfile.objects.create(user=self.teacher, department=UserProfile.Department.IT)
        UserProfile.objects.create(user=self.student, department=UserProfile.Department.IT)
        UserProfile.objects.create(
            user=self.other_student,
            department=UserProfile.Department.LIFE_SCIENCE,
        )
        self.quiz = Quiz.objects.create(
            teacher=self.teacher,
            title='Sample Quiz',
            description='A short quiz',
            is_active=True,
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            question_text='What is 2 + 2?',
            order=1,
        )
        self.correct_option = Option.objects.create(
            question=self.question,
            option_text='4',
            is_correct=True,
        )
        self.wrong_option = Option.objects.create(
            question=self.question,
            option_text='5',
            is_correct=False,
        )

    def test_completed_quiz_list_renders_result_link(self):
        result = QuizResult.objects.create(
            student=self.student,
            quiz=self.quiz,
            score=1,
            total_questions=1,
            percentage=100,
        )

        self.client.force_login(self.student)
        response = self.client.get(reverse('student_quiz_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Completed Quizzes')
        self.assertContains(response, reverse('quiz_result', args=[result.id]))

    def test_student_only_sees_same_department_quizzes(self):
        other_teacher = User.objects.create_user(
            username='life-science-teacher',
            password='password123',
            is_staff=True,
        )
        UserProfile.objects.create(
            user=other_teacher,
            department=UserProfile.Department.LIFE_SCIENCE,
        )
        other_quiz = Quiz.objects.create(
            teacher=other_teacher,
            title='Life Science Quiz',
            description='Hidden from IT students',
            is_active=True,
        )

        self.client.force_login(self.student)
        response = self.client.get(reverse('student_quiz_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.quiz.title)
        self.assertNotContains(response, other_quiz.title)

    def test_student_cannot_take_other_department_quiz(self):
        self.client.force_login(self.other_student)

        response = self.client.get(reverse('take_quiz', args=[self.quiz.id]))

        self.assertEqual(response.status_code, 404)

    def test_register_creates_department_profile(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'new-teacher',
                'email': 'new-teacher@example.com',
                'user_type': 'teacher',
                'department': UserProfile.Department.LIFE_SCIENCE,
                'password1': 'strong-password-123',
                'password2': 'strong-password-123',
            },
        )

        user = User.objects.get(username='new-teacher')
        self.assertRedirects(response, reverse('teacher_dashboard'))
        self.assertTrue(user.is_staff)
        self.assertEqual(user.profile.department, UserProfile.Department.LIFE_SCIENCE)

    def test_delete_quiz_requires_post(self):
        self.client.force_login(self.teacher)

        get_response = self.client.get(reverse('delete_quiz', args=[self.quiz.id]))
        self.assertEqual(get_response.status_code, 405)
        self.assertTrue(Quiz.objects.filter(id=self.quiz.id).exists())

        post_response = self.client.post(reverse('delete_quiz', args=[self.quiz.id]))
        self.assertRedirects(post_response, reverse('teacher_dashboard'))
        self.assertFalse(Quiz.objects.filter(id=self.quiz.id).exists())

    def test_quiz_requires_all_questions_before_creating_result(self):
        Question.objects.create(
            quiz=self.quiz,
            question_text='Unanswered question',
            order=2,
        )
        self.client.force_login(self.student)

        response = self.client.post(
            reverse('take_quiz', args=[self.quiz.id]),
            {f'question_{self.question.id}': str(self.correct_option.id)},
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(QuizResult.objects.filter(student=self.student, quiz=self.quiz).exists())
        self.assertContains(response, 'Please answer every question')

    def test_option_from_another_question_is_rejected(self):
        other_question = Question.objects.create(
            quiz=self.quiz,
            question_text='Other question',
            order=2,
        )
        forged_option = Option.objects.create(
            question=other_question,
            option_text='Forged correct answer',
            is_correct=True,
        )
        self.client.force_login(self.student)

        response = self.client.post(
            reverse('take_quiz', args=[self.quiz.id]),
            {f'question_{self.question.id}': str(forged_option.id)},
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(QuizResult.objects.filter(student=self.student, quiz=self.quiz).exists())
        self.assertContains(response, 'Please answer every question')
