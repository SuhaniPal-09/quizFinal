from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Quiz, Question, Option, UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher')])
    department = forms.ChoiceField(choices=UserProfile.Department.choices)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 'department']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get('user_type')
        user.is_staff = (user_type == 'teacher')
        if commit:
            user.save()
            UserProfile.objects.update_or_create(
                user=user,
                defaults={'department': self.cleaned_data.get('department')}
            )
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quiz title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quiz description',
                'rows': 4
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your question',
                'rows': 3
            })
        }


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_text', 'is_correct']
        widgets = {
            'option_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter option'
            }),
            'is_correct': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class OptionFormSet(forms.BaseModelFormSet):
    def clean(self):
        super().clean()
        if any(self.errors):
            return
        
        checked = sum(1 for form in self.forms if form.cleaned_data.get('is_correct'))
        if checked != 1:
            raise forms.ValidationError("Please select exactly one correct option.")
