from django.urls import path
from . import views

urlpatterns = [
    # Auth URLs
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    
    # Teacher URLs
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/create-quiz/', views.create_quiz, name='create_quiz'),
    path('teacher/edit-quiz/<int:quiz_id>/', views.edit_quiz, name='edit_quiz'),
    path('teacher/add-question/<int:quiz_id>/', views.add_question, name='add_question'),
    path('teacher/delete-question/<int:question_id>/', views.delete_question, name='delete_question'),
    path('teacher/delete-quiz/<int:quiz_id>/', views.delete_quiz, name='delete_quiz'),
    
    # Student URLs
    path('student/quizzes/', views.student_quiz_list, name='student_quiz_list'),
    path('student/take-quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('student/result/<int:result_id>/', views.quiz_result, name='quiz_result'),
]
