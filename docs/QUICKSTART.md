# 🚀 Quick Start Guide - Django Quiz App

## 5 Minute Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

---

## Step 1: Create Project Folder

```bash
mkdir quiz_app
cd quiz_app
```

---

## Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal now.

---

## Step 3: Install Django

```bash
pip install Django==4.2.0
```

---

## Step 4: Create Django Project & App

```bash
django-admin startproject quiz_project .
python manage.py startapp quiz_app
```

---

## Step 5: Copy Files to Your Project

Copy these files to your project:

1. **models.py** → `quiz_app/models.py`
2. **views.py** → `quiz_app/views.py`
3. **forms.py** → `quiz_app/forms.py`
4. **admin.py** → `quiz_app/admin.py`
5. **apps.py** → `quiz_app/apps.py`
6. **settings.py** → `quiz_project/settings.py` (REPLACE)
7. **urls_project.py** → `quiz_project/urls.py` (RENAME and REPLACE)
8. **urls_app.py** → `quiz_app/urls.py` (RENAME)

---

## Step 6: Create Templates & Static Folder

```bash
mkdir quiz_app/templates
mkdir quiz_app/static
```

Copy all `.html` files to `quiz_app/templates/`
Copy `style.css` to `quiz_app/static/style.css`

---

## Step 7: Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Step 8: Create Admin Account

```bash
python manage.py createsuperuser
```

Follow prompts to create your admin account.

---

## Step 9: Run Server

```bash
python manage.py runserver
```

---

## Access Your App

- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## First Time Usage

### Create a Teacher Account
1. Go to http://127.0.0.1:8000/
2. Click "Register"
3. Fill in details and select "Teacher" as user type
4. Login with teacher account

### Create a Quiz
1. Click "Create New Quiz"
2. Enter title and description
3. Check "Active" checkbox
4. Click "Create Quiz"
5. Click "Edit" on your quiz
6. Click "+ Add Question"
7. Enter question and 4 options
8. Check the correct option
9. Click "Save Question"

### Create a Student Account
1. Logout (top right)
2. Click "Register"
3. Select "Student" as user type
4. Login with student account

### Take a Quiz
1. Student sees available quizzes
2. Click "Take Quiz"
3. Answer all questions
4. Click "Submit Quiz"
5. View results and review answers

---

## File Placement

```
quiz_app/
├── migrations/
│   └── __init__.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── teacher_dashboard.html
│   ├── create_quiz.html
│   ├── edit_quiz.html
│   ├── add_question.html
│   ├── student_quiz_list.html
│   ├── take_quiz.html
│   └── result.html
├── static/
│   └── style.css
├── __init__.py
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── urls.py
└── views.py

quiz_project/
├── __init__.py
├── settings.py
├── urls.py
└── wsgi.py

manage.py
db.sqlite3
```

---

## Troubleshooting

**Error: "No such table"**
```bash
python manage.py migrate
```

**Error: "ModuleNotFoundError: No module named 'django'"**
```bash
pip install Django==4.2.0
```

**Port 8000 is in use**
```bash
python manage.py runserver 8080
```

**Static files not loading**
1. Check if you have `style.css` in `quiz_app/static/`
2. Run: `python manage.py collectstatic --noinput`

---

## Features Checklist

✅ User Registration (Student/Teacher)
✅ User Login/Logout
✅ Teacher Dashboard
✅ Create Quiz
✅ Add Questions with 4 Options
✅ Mark Correct Answer
✅ Student Quiz List
✅ Take Quiz
✅ Auto Scoring
✅ View Results
✅ Review Answers
✅ Admin Panel
✅ SQLite Database
✅ Bootstrap Responsive Design

---

## Database Tables Created

1. **auth_user** - Django default user table
2. **quiz_app_quiz** - Quiz data
3. **quiz_app_question** - Questions
4. **quiz_app_option** - Multiple choice options
5. **quiz_app_studentanswer** - Student responses
6. **quiz_app_quizresult** - Quiz scores

---

## Next Steps

1. ✅ Complete the setup above
2. ✅ Create a teacher account and a quiz
3. ✅ Create a student account
4. ✅ Take the quiz as a student
5. ✅ Review the code to understand how it works
6. ✅ Customize colors/styling in `style.css`
7. ✅ Add more features as needed

---

## Commands Reference

```bash
# Activate virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Deactivate virtual environment
deactivate

# Run server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Create static files folder
python manage.py collectstatic

# List all URLs
python manage.py show_urls
```

---

Happy Quizzing! 🎉📚
