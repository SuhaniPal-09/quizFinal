from django.contrib import admin
from .models import Quiz, Question, Option, StudentAnswer, QuizResult, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'department']
    list_filter = ['department']
    search_fields = ['user__username', 'user__email']


class OptionInline(admin.TabularInline):
    model = Option
    extra = 4


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'is_active', 'created_at', 'question_count']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'teacher__username']
    inlines = [QuestionInline]
    
    def question_count(self, obj):
        return obj.questions.count()
    question_count.short_description = 'Questions'


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'quiz', 'order']
    list_filter = ['quiz']
    search_fields = ['question_text']
    inlines = [OptionInline]


class OptionAdmin(admin.ModelAdmin):
    list_display = ['option_text', 'question', 'is_correct']
    list_filter = ['is_correct']
    search_fields = ['option_text']


class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ['student', 'quiz', 'question', 'answered_at']
    list_filter = ['quiz', 'answered_at']
    search_fields = ['student__username']
    readonly_fields = ['student', 'quiz', 'question', 'answered_at']


class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'quiz', 'score', 'total_questions', 'percentage', 'completed_at']
    list_filter = ['quiz', 'completed_at']
    search_fields = ['student__username', 'quiz__title']
    readonly_fields = ['student', 'quiz', 'score', 'total_questions', 'percentage', 'completed_at']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(StudentAnswer, StudentAnswerAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
