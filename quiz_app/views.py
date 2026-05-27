from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Quiz, Question, Option, StudentAnswer, QuizResult, UserProfile
from .forms import UserRegisterForm, LoginForm, QuizForm


def get_user_profile(user):
    profile, _ = UserProfile.objects.get_or_create(user=user)
    return profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            if form.cleaned_data.get('user_type') == 'teacher':
                return redirect('teacher_dashboard')
            else:
                return redirect('student_quiz_list')
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('teacher_dashboard')
        else:
            return redirect('student_quiz_list')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('teacher_dashboard')
                else:
                    return redirect('student_quiz_list')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    if request.user.is_staff:
        return redirect('teacher_dashboard')
    else:
        return redirect('student_quiz_list')


# Teacher Views
@login_required(login_url='login')
def teacher_dashboard(request):
    if not request.user.is_staff:
        return redirect('student_quiz_list')
    
    profile = get_user_profile(request.user)
    quizzes = Quiz.objects.filter(teacher=request.user)
    return render(request, 'teacher_dashboard.html', {
        'quizzes': quizzes,
        'department_name': profile.get_department_display(),
    })


@login_required(login_url='login')
def create_quiz(request):
    if not request.user.is_staff:
        return redirect('student_quiz_list')
    
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.teacher = request.user
            quiz.save()
            return redirect('edit_quiz', quiz_id=quiz.id)
    else:
        form = QuizForm()
    
    return render(request, 'create_quiz.html', {'form': form})


@login_required(login_url='login')
def edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, teacher=request.user)
    questions = quiz.questions.all()
    
    return render(request, 'edit_quiz.html', {
        'quiz': quiz,
        'questions': questions
    })


@login_required(login_url='login')
def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, teacher=request.user)
    form_data = request.POST if request.method == 'POST' else {}
    
    if request.method == 'POST':
        question_text = request.POST.get('question_text', '').strip()
        options_data = []
        
        for i in range(1, 5):
            option_text = request.POST.get(f'option_{i}', '').strip()
            is_correct = request.POST.get(f'correct_{i}') == 'on'
            if option_text:
                options_data.append({
                    'text': option_text,
                    'is_correct': is_correct
                })
        
        if question_text and len(options_data) == 4:
            correct_count = sum(1 for opt in options_data if opt['is_correct'])
            if correct_count == 1:
                question = Question.objects.create(
                    quiz=quiz,
                    question_text=question_text,
                    order=quiz.questions.count() + 1
                )
                
                for opt_data in options_data:
                    Option.objects.create(
                        question=question,
                        option_text=opt_data['text'],
                        is_correct=opt_data['is_correct']
                    )
                
                return redirect('edit_quiz', quiz_id=quiz.id)
            messages.error(request, 'Please select exactly one correct answer.')
        else:
            messages.error(request, 'Please enter a question and all four answer options.')
    
    option_fields = [
        {
            'number': i,
            'text': form_data.get(f'option_{i}', ''),
            'is_correct': form_data.get(f'correct_{i}') == 'on',
        }
        for i in range(1, 5)
    ]

    return render(request, 'add_question.html', {
        'quiz': quiz,
        'question_text': form_data.get('question_text', ''),
        'option_fields': option_fields,
    })


@login_required(login_url='login')
@require_POST
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    quiz = question.quiz
    
    if quiz.teacher != request.user:
        return redirect('teacher_dashboard')
    
    quiz_id = quiz.id
    question.delete()
    messages.success(request, 'Question deleted.')
    
    return redirect('edit_quiz', quiz_id=quiz_id)


@login_required(login_url='login')
@require_POST
def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, teacher=request.user)
    quiz.delete()
    messages.success(request, 'Quiz deleted.')
    return redirect('teacher_dashboard')


# Student Views
@login_required(login_url='login')
def student_quiz_list(request):
    if request.user.is_staff:
        return redirect('teacher_dashboard')
    
    profile = get_user_profile(request.user)
    quizzes = Quiz.objects.filter(
        is_active=True,
        teacher__profile__department=profile.department,
    ).select_related('teacher', 'teacher__profile')
    
    # Get user's results
    results = QuizResult.objects.filter(
        student=request.user,
        quiz__teacher__profile__department=profile.department,
    ).select_related('quiz', 'quiz__teacher', 'quiz__teacher__profile')
    completed_quiz_ids = results.values_list('quiz_id', flat=True)
    
    available_quizzes = quizzes.exclude(id__in=completed_quiz_ids)
    
    return render(request, 'student_quiz_list.html', {
        'available_quizzes': available_quizzes,
        'completed_results': results,
        'department_name': profile.get_department_display(),
    })


@login_required(login_url='login')
def take_quiz(request, quiz_id):
    if request.user.is_staff:
        return redirect('teacher_dashboard')
    
    profile = get_user_profile(request.user)
    quiz = get_object_or_404(
        Quiz,
        id=quiz_id,
        is_active=True,
        teacher__profile__department=profile.department,
    )
    
    # Check if already completed
    if QuizResult.objects.filter(student=request.user, quiz=quiz).exists():
        return redirect('student_quiz_list')
    
    questions = quiz.questions.all()
    if not questions.exists():
        messages.error(request, 'This quiz does not have any questions yet.')
        return redirect('student_quiz_list')
    
    if request.method == 'POST':
        score = 0
        total = questions.count()
        missing_questions = []
        
        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            
            if selected_option_id:
                try:
                    option = question.options.get(id=selected_option_id)
                    
                    StudentAnswer.objects.update_or_create(
                        student=request.user,
                        quiz=quiz,
                        question=question,
                        defaults={'selected_option': option}
                    )
                    
                    if option.is_correct:
                        score += 1
                except Option.DoesNotExist:
                    missing_questions.append(question.id)
            else:
                missing_questions.append(question.id)
        
        if missing_questions:
            messages.error(request, 'Please answer every question before submitting the quiz.')
            return render(request, 'take_quiz.html', {
                'quiz': quiz,
                'questions': questions,
                'selected_option_ids': set(request.POST.values()),
            })
        
        percentage = (score / total * 100) if total > 0 else 0
        
        result = QuizResult.objects.create(
            student=request.user,
            quiz=quiz,
            score=score,
            total_questions=total,
            percentage=percentage
        )
        
        return redirect('quiz_result', result_id=result.id)
    
    return render(request, 'take_quiz.html', {
        'quiz': quiz,
        'questions': questions,
        'selected_option_ids': set(),
    })


@login_required(login_url='login')
def quiz_result(request, result_id):
    if request.user.is_staff:
        return redirect('teacher_dashboard')
    
    result = get_object_or_404(QuizResult, id=result_id, student=request.user)
    answers = StudentAnswer.objects.filter(student=request.user, quiz=result.quiz)
    questions = result.quiz.questions.all()
    
    question_answers = []
    for question in questions:
        answer = answers.filter(question=question).first()
        question_answers.append({
            'question': question,
            'user_answer': answer,
            'correct_option': question.options.filter(is_correct=True).first()
        })
    
    return render(request, 'result.html', {
        'result': result,
        'question_answers': question_answers
    })
