from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Department(models.TextChoices):
        IT = 'it', 'IT Department'
        LIFE_SCIENCE = 'life_science', 'Life Science Department'
        COMMERCE = 'commerce', 'Commerce Department'
        ARTS = 'arts', 'Arts Department'
        SCIENCE = 'science', 'Science Department'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department = models.CharField(
        max_length=30,
        choices=Department.choices,
        default=Department.IT,
    )

    def __str__(self):
        return f"{self.user.username} - {self.get_department_display()}"

class Quiz(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question_text[:50]
    
    class Meta:
        ordering = ['order']


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.option_text[:50]


class StudentAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'question', 'quiz')


class QuizResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    percentage = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'quiz')
    
    def __str__(self):
        return f"{self.student.username} - {self.quiz.title}: {self.percentage}%"
