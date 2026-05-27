# 📁 Complete File Guide - Django Quiz App

## Overview

This document lists all files needed for the Django Quiz Application and their purposes.

---

## 🔧 Configuration Files (Project Root)

### `requirements.txt`
- **Purpose**: List of Python packages to install
- **Install with**: `pip install -r requirements.txt`
- **Contains**: Django==4.2.0, Pillow==10.0.0
- **Location**: Project root

---

## 🎛️ Django Project Files (`quiz_project/` folder)

### `quiz_project/settings.py`
- **Purpose**: Main Django configuration file
- **Contains**: 
  - Database configuration (SQLite)
  - Installed apps
  - Middleware
  - Template settings
  - Static files configuration
  - Secret key
- **Action**: REPLACE the auto-generated settings.py

### `quiz_project/urls.py`
- **Purpose**: Main URL routing configuration
- **Contains**: 
  - Admin URLs
  - App URLs
  - Static and media file serving
- **Filename**: Rename `urls_project.py` to `urls.py`
- **Action**: REPLACE the auto-generated urls.py

### `quiz_project/__init__.py`
- **Purpose**: Marks this folder as Python package
- **Action**: Keep empty (auto-generated)

### `quiz_project/wsgi.py`
- **Purpose**: WSGI configuration for deployment
- **Action**: Keep auto-generated (no changes needed)

### `manage.py`
- **Purpose**: Django management script
- **Action**: Keep auto-generated (no changes needed)

---

## 📱 Quiz App Files (`quiz_app/` folder)

### Core Application Files

#### `quiz_app/models.py`
- **Purpose**: Database model definitions
- **Models Defined**:
  - `Quiz` - Quiz basic info
  - `Question` - Quiz questions
  - `Option` - Multiple choice options
  - `StudentAnswer` - Student's submitted answers
  - `QuizResult` - Quiz score and results
- **Database**: Automatically creates 5 tables in SQLite

#### `quiz_app/views.py`
- **Purpose**: Business logic and request handling
- **Functions**:
  - Auth: register, login_view, logout_view
  - Teacher: teacher_dashboard, create_quiz, edit_quiz, add_question, delete_*
  - Student: student_quiz_list, take_quiz, quiz_result
- **Total**: 17 view functions

#### `quiz_app/forms.py`
- **Purpose**: Form validation and rendering
- **Forms**:
  - `UserRegisterForm` - Registration with user type
  - `LoginForm` - Login credentials
  - `QuizForm` - Quiz creation
  - `QuestionForm` - Question creation
  - `OptionForm` - Option creation
- **Validators**: Ensures exactly one correct answer per question

#### `quiz_app/urls.py`
- **Purpose**: App-specific URL routing
- **Routes**: 12 URL patterns for all views
- **Filename**: Rename `urls_app.py` to `urls.py`

#### `quiz_app/admin.py`
- **Purpose**: Django admin interface customization
- **Admin Classes**: Custom admins for all models
- **Features**:
  - List displays
  - Filters
  - Search fields
  - Inline editing

#### `quiz_app/apps.py`
- **Purpose**: App configuration
- **Contains**: App name and verbose name

#### `quiz_app/__init__.py`
- **Purpose**: Marks folder as Python package
- **Action**: Keep empty

---

## 🎨 Template Files (`quiz_app/templates/` folder)

All templates use Bootstrap 5 and inherit from `base.html`

### `base.html`
- **Purpose**: Base template with navbar and footer
- **Used By**: All other templates extend this
- **Contains**: Navbar, message alerts, footer
- **Features**: Responsive navigation

### `login.html`
- **Purpose**: User login page
- **Features**:
  - Username input
  - Password input
  - Login button
  - Register link
- **Access**: Public (non-authenticated users)

### `register.html`
- **Purpose**: User registration page
- **Features**:
  - Username input
  - Email input
  - User type selector (Student/Teacher)
  - Password fields
  - Confirmation
- **Access**: Public

### `teacher_dashboard.html`
- **Purpose**: Main teacher interface
- **Features**:
  - List all quizzes
  - Quiz cards with info
  - Edit/Delete buttons
  - Create new quiz button
- **Access**: Teachers only

### `create_quiz.html`
- **Purpose**: Create new quiz form
- **Fields**:
  - Quiz title
  - Description
  - Active checkbox
- **Action**: Redirects to edit_quiz after creation

### `edit_quiz.html`
- **Purpose**: Manage quiz questions
- **Shows**:
  - Quiz title and description
  - List of all questions
  - Options for each question
  - Delete question button
  - Add question button
- **Access**: Teachers only (for their quizzes)

### `add_question.html`
- **Purpose**: Add new question to quiz
- **Fields**:
  - Question text
  - 4 Option text fields
  - Checkboxes for correct answer
- **Validation**: Ensures exactly 1 correct answer

### `student_quiz_list.html`
- **Purpose**: View available and completed quizzes
- **Sections**:
  - Available Quizzes to take
  - Completed Quizzes with scores
- **Access**: Students only

### `take_quiz.html`
- **Purpose**: Interactive quiz interface
- **Features**:
  - Question display
  - Radio button options
  - Question counter
  - Form validation (all questions required)
  - Submit button
- **Access**: Students only

### `result.html`
- **Purpose**: Show quiz results and review
- **Shows**:
  - Score (e.g., 7/10)
  - Percentage
  - Each question with:
    - Student's answer
    - Correct answer
    - Status (Correct/Incorrect)
- **Access**: Students (their own results)

---

## 🎨 Static Files (`quiz_app/static/` folder)

### `style.css`
- **Purpose**: All custom styling
- **Features**:
  - Bootstrap 5 integration
  - Custom color variables
  - Component styling (cards, buttons, forms)
  - Responsive design
  - Animations and hover effects
- **Size**: ~700 lines
- **Color Variables**:
  - Primary: #3498db
  - Secondary: #2ecc71
  - Danger: #e74c3c

---

## 📚 Documentation Files

### `README.md`
- **Purpose**: Complete project documentation
- **Contains**:
  - Features list
  - Project structure
  - Installation steps
  - Usage guide
  - Database schema
  - Technologies
  - Troubleshooting
  - Future enhancements

### `QUICKSTART.md`
- **Purpose**: Fast setup guide
- **Contains**: 9 quick steps to get started
- **Time**: ~5 minutes to setup

### `quiz_app_setup.md`
- **Purpose**: Project structure overview

---

## 🗂️ Directory Structure Reference

```
quiz_project/                    # Main project folder
│
├── quiz_project/               # Django project configuration
│   ├── __init__.py
│   ├── settings.py             # ⭐ REPLACE with provided file
│   ├── urls.py                 # ⭐ REPLACE with urls_project.py
│   └── wsgi.py
│
├── quiz_app/                   # Main Django app
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── templates/              # HTML templates
│   │   ├── base.html           # ⭐ Copy from files
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── teacher_dashboard.html
│   │   ├── create_quiz.html
│   │   ├── edit_quiz.html
│   │   ├── add_question.html
│   │   ├── student_quiz_list.html
│   │   ├── take_quiz.html
│   │   └── result.html
│   │
│   ├── static/                 # CSS and static files
│   │   └── style.css           # ⭐ Copy from files
│   │
│   ├── __init__.py
│   ├── admin.py                # ⭐ Copy from files
│   ├── apps.py                 # ⭐ Copy from files
│   ├── forms.py                # ⭐ Copy from files
│   ├── models.py               # ⭐ Copy from files
│   ├── urls.py                 # ⭐ Copy from urls_app.py
│   └── views.py                # ⭐ Copy from files
│
├── manage.py                   # Django CLI
├── db.sqlite3                  # Database (auto-created)
└── requirements.txt            # ⭐ Copy from files
```

---

## 📋 File Checklist

Before starting, ensure you have:

```
Core Configuration:
  ☐ requirements.txt
  ☐ quiz_project/settings.py
  ☐ quiz_project/urls.py

App Core:
  ☐ quiz_app/models.py
  ☐ quiz_app/views.py
  ☐ quiz_app/forms.py
  ☐ quiz_app/urls.py
  ☐ quiz_app/admin.py
  ☐ quiz_app/apps.py

Templates (9 files):
  ☐ quiz_app/templates/base.html
  ☐ quiz_app/templates/login.html
  ☐ quiz_app/templates/register.html
  ☐ quiz_app/templates/teacher_dashboard.html
  ☐ quiz_app/templates/create_quiz.html
  ☐ quiz_app/templates/edit_quiz.html
  ☐ quiz_app/templates/add_question.html
  ☐ quiz_app/templates/student_quiz_list.html
  ☐ quiz_app/templates/take_quiz.html
  ☐ quiz_app/templates/result.html

Static:
  ☐ quiz_app/static/style.css

Documentation:
  ☐ README.md
  ☐ QUICKSTART.md
```

---

## 📝 File Sizes (Approximate)

| File | Size | Lines |
|------|------|-------|
| models.py | 2 KB | 60 |
| views.py | 8 KB | 240 |
| forms.py | 3 KB | 80 |
| admin.py | 3 KB | 85 |
| urls.py | 1 KB | 20 |
| style.css | 10 KB | 400 |
| settings.py | 3 KB | 90 |
| All templates | 15 KB | 600 |
| **Total** | **~50 KB** | **~1700** |

---

## 🔐 Important Notes

1. **settings.py**
   - Change `SECRET_KEY` before production
   - Set `DEBUG = False` before deployment

2. **Database**
   - Uses SQLite (auto-created as db.sqlite3)
   - For production, use PostgreSQL or MySQL

3. **Static Files**
   - Run `python manage.py collectstatic` before deployment
   - Bootstrap CSS loaded from CDN (requires internet)

4. **Media Files**
   - App supports media uploads (folder created automatically)
   - Currently not used, ready for future features

---

## 🚀 Quick Reference

| Task | File to Edit |
|------|--------------|
| Change app name | settings.py (INSTALLED_APPS) |
| Change colors | style.css (:root) |
| Change database | settings.py (DATABASES) |
| Add new views | views.py |
| Add new models | models.py |
| Change URLs | urls.py |
| Modify templates | templates/*.html |
| Customize forms | forms.py |

---

Happy Coding! 🎉
