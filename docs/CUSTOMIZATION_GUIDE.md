# 🎨 Customization Guide - Django Quiz App

Learn how to customize the Quiz App to match your needs.

---

## 🎨 Visual Customization

### Change Colors

Edit `quiz_app/static/style.css` at the top:

```css
:root {
    --primary-color: #3498db;      /* Blue - Main color */
    --secondary-color: #2ecc71;    /* Green - Success/Correct */
    --danger-color: #e74c3c;       /* Red - Error/Delete */
    --dark-color: #2c3e50;         /* Dark - Text */
    --light-color: #ecf0f1;        /* Light - Background */
    --border-radius: 6px;          /* Button/Card corners */
}
```

### Change App Title

In `quiz_app/templates/base.html`:

```html
<!-- Change this line -->
<a class="navbar-brand" href="{% url 'home' %}">
    📚 Quiz App
</a>

<!-- To this -->
<a class="navbar-brand" href="{% url 'home' %}">
    🎓 My School Quiz System
</a>
```

### Change Footer Text

In `quiz_app/templates/base.html` (bottom):

```html
<footer>
    <p>&copy; 2024 Quiz App. All Rights Reserved.</p>
</footer>

<!-- Change to -->
<footer>
    <p>&copy; 2024 Your School Name. All Rights Reserved.</p>
</footer>
```

### Change Page Titles

In each template, modify:

```html
{% block title %}Quiz App - Login{% endblock %}
```

---

## 📝 Text & Content Customization

### Change Login Page Text

In `quiz_app/templates/login.html`:

```html
<div class="card-header">
    Login
</div>

<!-- Change to -->
<div class="card-header">
    Sign In to Your Account
</div>
```

### Change Button Text

Search for button text in templates and replace:

```html
<button type="submit" class="btn btn-primary">
    Login
</button>

<!-- Change to -->
<button type="submit" class="btn btn-primary">
    Sign In
</button>
```

### Add Welcome Message

In `quiz_app/templates/teacher_dashboard.html`:

```html
<p class="text-muted">Manage your quizzes and view student results</p>

<!-- Add after this line -->
<p class="alert alert-info">Welcome! Create quizzes and monitor student progress.</p>
```

---

## 🔧 Functional Customization

### Change Database

Edit `quiz_project/settings.py`:

```python
# Current (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Change to PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'quiz_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Change Questions Per Quiz

The current app uses a simple counter. To change:

In `quiz_app/views.py` (add_question function):

```python
# Modify the form to limit questions
MAX_QUESTIONS = 20  # Add at top

# In add_question view:
if quiz.questions.count() >= MAX_QUESTIONS:
    return redirect('edit_quiz', quiz_id=quiz.id)
```

### Change Options Per Question

To allow more than 4 options:

Edit `quiz_app/templates/add_question.html`:

```html
{% for i in "12345" %}  <!-- Was "1234", now allows 5 options -->
```

And update `quiz_app/views.py` add_question function:

```python
for i in range(1, 6):  # Was range(1, 5)
    option_text = request.POST.get(f'option_{i}')
    is_correct = request.POST.get(f'correct_{i}') == 'on'
```

### Add Quiz Timer

In `quiz_app/templates/take_quiz.html`, add before closing tags:

```html
<script>
    // Set timer for 10 minutes
    const QUIZ_TIME = 10 * 60; // seconds
    let timeRemaining = QUIZ_TIME;
    
    const timer = setInterval(() => {
        timeRemaining--;
        
        if (timeRemaining <= 0) {
            clearInterval(timer);
            document.getElementById('quiz_form').submit();
            alert('Time is up! Quiz submitted automatically.');
        }
        
        // Display timer (optional)
        console.log(`Time remaining: ${Math.floor(timeRemaining / 60)}:${timeRemaining % 60}`);
    }, 1000);
</script>
```

---

## 🗄️ Data & Model Customization

### Add Question Categories

Edit `quiz_app/models.py`:

```python
class Question(models.Model):
    CATEGORY_CHOICES = [
        ('math', 'Mathematics'),
        ('science', 'Science'),
        ('history', 'History'),
        ('english', 'English'),
    ]
    
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    order = models.IntegerField(default=0)
```

Then migrate:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Add Difficulty Levels

Edit `quiz_app/models.py`:

```python
class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
```

### Add Question Points

Edit `quiz_app/models.py`:

```python
class Question(models.Model):
    points = models.IntegerField(default=1)  # Add this field
```

Update scoring in `views.py`:

```python
# Old scoring
if option.is_correct:
    score += 1

# New scoring with points
if option.is_correct:
    score += question.points
```

---

## 👥 Permission Customization

### Make Quiz Private

Edit `quiz_app/models.py`:

```python
class Quiz(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)  # Add this
```

Update `views.py`:

```python
def student_quiz_list(request):
    quizzes = Quiz.objects.filter(is_active=True, is_private=False)
    # ... rest of code
```

### Add Quiz Access Control

Allow only specific students:

```python
# Add to models.py
class QuizAccess(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    granted_at = models.DateTimeField(auto_now_add=True)
```

---

## 🎯 Feature Customization

### Add Quiz Retake Option

Edit `quiz_app/models.py`:

```python
class Quiz(models.Model):
    allow_retake = models.BooleanField(default=True)
```

Update `views.py`:

```python
def take_quiz(request, quiz_id):
    # Check if already completed
    result = QuizResult.objects.filter(student=request.user, quiz=quiz).first()
    
    if result and not quiz.allow_retake:
        return redirect('student_quiz_list')
```

### Add Negative Marking

Edit `views.py`:

```python
for question in questions:
    selected_option_id = request.POST.get(f'question_{question.id}')
    
    if selected_option_id:
        option = Option.objects.get(id=selected_option_id)
        
        if option.is_correct:
            score += 1
        else:
            score -= 0.25  # Negative marking
```

### Add Leaderboard

Create new view in `views.py`:

```python
@login_required(login_url='login')
def leaderboard(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    results = QuizResult.objects.filter(quiz=quiz).order_by('-percentage', '-score')[:10]
    
    return render(request, 'leaderboard.html', {
        'quiz': quiz,
        'results': results
    })
```

Add URL:
```python
# In quiz_app/urls.py
path('student/leaderboard/<int:quiz_id>/', views.leaderboard, name='leaderboard'),
```

---

## 📊 Admin Customization

### Customize Admin View

Edit `quiz_app/admin.py`:

```python
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'is_active', 'created_at']
    
    # Add filters
    list_filter = ['is_active', 'created_at', 'teacher']
    
    # Add search
    search_fields = ['title', 'description']
    
    # Add readonly
    readonly_fields = ['created_at']
    
    # Add fieldsets
    fieldsets = (
        ('Quiz Information', {
            'fields': ('title', 'description', 'teacher')
        }),
        ('Status', {
            'fields': ('is_active', 'created_at')
        }),
    )
```

---

## 🎨 UI Customization Examples

### Change Button Colors

In `style.css`:

```css
.btn-primary {
    background-color: var(--primary-color);  /* Change here */
}

.btn-success {
    background-color: var(--secondary-color);  /* Change here */
}
```

### Change Card Styling

In `style.css`:

```css
.card {
    border: none;
    border-radius: 8px;  /* Change corner radius */
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);  /* Change shadow */
    border-left: 4px solid var(--primary-color);  /* Add left border */
}
```

### Change Font

In `style.css`:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    /* Change to */
    font-family: 'Arial', sans-serif;
}
```

---

## 🔒 Security Customization

### Enable HTTPS

In `quiz_project/settings.py`:

```python
# For production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### Change Secret Key

In `settings.py`:

```python
SECRET_KEY = 'your-new-secret-key-here'
```

Generate a secure key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📧 Email Customization

Add email notifications:

```python
# In settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

---

## 🚀 Performance Customization

### Enable Caching

In `settings.py`:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-location',
    }
}
```

### Database Optimization

Add indexes in `models.py`:

```python
class Quiz(models.Model):
    # ... fields ...
    
    class Meta:
        indexes = [
            models.Index(fields=['teacher', 'is_active']),
        ]
```

---

## 📱 Mobile Customization

Bootstrap is already responsive. For more mobile-friendly:

In `quiz_app/templates/base.html`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
```

Add mobile menu icon:

```css
/* In style.css */
@media (max-width: 768px) {
    .navbar {
        padding: 10px 0;
    }
    
    .quiz-grid {
        grid-template-columns: 1fr;
    }
}
```

---

## ✅ Common Customizations Checklist

- [ ] Change app title/branding
- [ ] Change color scheme
- [ ] Change footer text
- [ ] Customize button labels
- [ ] Add logo
- [ ] Change database (optional)
- [ ] Add question categories
- [ ] Enable quiz retakes
- [ ] Add negative marking
- [ ] Customize admin interface
- [ ] Add email notifications (optional)
- [ ] Optimize for mobile
- [ ] Change font
- [ ] Add security features
- [ ] Add leaderboard

---

## 💡 Tips for Customization

1. **Always backup** before making changes
2. **Test locally** before deploying
3. **Document your changes** for future reference
4. **Use browser dev tools** (F12) to test CSS changes
5. **Create branches** if using version control
6. **Test on mobile** for responsive design
7. **Keep performance** in mind for large databases

---

## 🆘 Rollback Changes

If something breaks:

1. Close without saving (in editor)
2. Or use Git: `git checkout filename`
3. Or restore from backup
4. Or manually revert changes

---

Happy Customizing! 🎉

