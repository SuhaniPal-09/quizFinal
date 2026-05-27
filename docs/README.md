# Django Quiz Application

A simple and clean quiz application built with Django where teachers can create quizzes and students can take them. Features include MCQ (multiple choice questions) with 4 options, user authentication, score tracking, and answer review.

## Features

✅ User Authentication (Student/Teacher signup and login)
✅ Teacher Dashboard - Create and manage quizzes
✅ Quiz Creation - Add questions with 4 multiple choice options
✅ Student Dashboard - Browse and take available quizzes
✅ Quiz Taking - Interactive quiz interface
✅ Results & Review - View score and review answers
✅ SQLite Database
✅ Bootstrap 5 Responsive Design
✅ Simple and Clean UI

## Project Structure

```
quiz_project/
│
├── quiz_project/
│   ├── __init__.py
│   ├── settings.py          # Main configuration
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py
│
├── quiz_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── teacher_dashboard.html
│   │   ├── create_quiz.html
│   │   ├── edit_quiz.html
│   │   ├── add_question.html
│   │   ├── student_quiz_list.html
│   │   ├── take_quiz.html
│   │   └── result.html
│   ├── static/
│   │   └── style.css
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│
├── manage.py
├── db.sqlite3               # Database (created after migration)
└── requirements.txt
```

## Installation & Setup

### Step 1: Create Project Directory

```bash
mkdir quiz_project
cd quiz_project
```

### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create Django Project & App

```bash
# Create project
django-admin startproject quiz_project .

# Create app
python manage.py startapp quiz_app
```

### Step 5: Add Files

1. Replace `quiz_project/settings.py` with the provided `settings.py`
2. Replace `quiz_project/urls.py` with the provided `urls_project.py`
3. Copy `models.py`, `views.py`, `forms.py`, `admin.py` to `quiz_app/`
4. Create `quiz_app/urls.py` with the provided `urls_app.py`
5. Create `quiz_app/static/style.css` with the provided `style.css`
6. Create `quiz_app/templates/` folder and add all `.html` files

### Step 6: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 8: Run Development Server

```bash
python manage.py runserver
```

The app will be available at: `http://127.0.0.1:8000/`

## Usage

### For Students

1. **Register**: Go to the register page and sign up as a Student
2. **Login**: Use your credentials to login
3. **Browse Quizzes**: View available quizzes on your dashboard
4. **Take Quiz**: Click on a quiz to start answering questions
5. **View Results**: See your score and review your answers after submission
6. **View History**: See your completed quizzes and scores

### For Teachers

1. **Register**: Go to the register page and sign up as a Teacher
2. **Login**: Use your credentials to login
3. **Create Quiz**: Click "Create New Quiz" and fill in the details
4. **Add Questions**: After creating a quiz, add questions with 4 options each
5. **Mark Correct Answer**: Select the correct option for each question
6. **Activate Quiz**: Make sure the quiz is marked as "Active" so students can take it
7. **Manage Quizzes**: Edit or delete quizzes from the dashboard

## URLs

### Public URLs
- `/` - Login page
- `/register/` - Registration page

### Teacher URLs
- `/teacher/dashboard/` - Teacher dashboard (view all quizzes)
- `/teacher/create-quiz/` - Create a new quiz
- `/teacher/edit-quiz/<quiz_id>/` - Edit quiz and manage questions
- `/teacher/add-question/<quiz_id>/` - Add a question to a quiz
- `/teacher/delete-question/<question_id>/` - Delete a question
- `/teacher/delete-quiz/<quiz_id>/` - Delete a quiz

### Student URLs
- `/student/quizzes/` - View available quizzes
- `/student/take-quiz/<quiz_id>/` - Take a quiz
- `/student/result/<result_id>/` - View quiz result

### Admin
- `/admin/` - Django admin panel

## Database Models

### Quiz
- teacher (ForeignKey to User)
- title
- description
- created_at
- is_active

### Question
- quiz (ForeignKey)
- question_text
- order

### Option
- question (ForeignKey)
- option_text
- is_correct

### StudentAnswer
- student (ForeignKey to User)
- quiz (ForeignKey)
- question (ForeignKey)
- selected_option (ForeignKey)
- answered_at

### QuizResult
- student (ForeignKey to User)
- quiz (ForeignKey)
- score
- total_questions
- percentage
- completed_at

## Technologies Used

- **Backend**: Django 4.2
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **JavaScript**: Vanilla JS for form validation

## Default Admin Account

After running `createsuperuser`, you can login to the admin panel at `/admin/` with your credentials.

## Key Features Explained

### Quiz Creation Flow
1. Teacher creates a quiz with title and description
2. Teacher adds questions one by one
3. For each question, teacher provides exactly 4 options
4. Teacher marks exactly one option as correct
5. Quiz becomes available to students once marked as "Active"

### Quiz Taking Flow
1. Student selects a quiz from available list
2. Questions are displayed one by one
3. Student selects one option for each question
4. All questions must be answered before submission
5. After submission, student can see their score and review answers

### Scoring System
- Each correct answer = 1 point
- Score = (Correct Answers / Total Questions) * 100
- Score is displayed as percentage

## Notes

- This is a simple implementation suitable for learning and small-scale use
- For production, change `DEBUG = False` in settings.py
- Change `SECRET_KEY` to a secure random key
- Use a proper database like PostgreSQL
- Add CSRF protection and security headers
- Implement proper authentication and authorization checks

## Troubleshooting

### "No such table" error
```bash
python manage.py migrate
```

### Static files not loading
```bash
python manage.py collectstatic
```

### Port already in use
```bash
python manage.py runserver 8080
```

### Database locked
Delete `db.sqlite3` and run migrations again (only in development)

## Future Enhancements

- Timer for quizzes
- Question randomization
- Multiple correct answers per question
- Difficulty levels
- Question categories
- Negative marking
- Leaderboard for students
- Export results to CSV
- Question bank management
- Quiz scheduling

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, check the Django and Bootstrap documentation:
- Django: https://docs.djangoproject.com/
- Bootstrap: https://getbootstrap.com/docs/

---

Happy Quiz Taking! 📚✨
