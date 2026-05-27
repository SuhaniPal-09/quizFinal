# 🚀 Django Quiz App - Ready to Use!

## Quick Start (2 Minutes)

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Admin User
```bash
python manage.py createsuperuser
```

### 4. Run Server
```bash
python manage.py runserver
```

### 5. Access App
- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

---

## 📚 Documentation

See the `docs/` folder for:
- **QUICKSTART.md** - Full setup guide
- **README.md** - Complete documentation
- **INSTALLATION_CHECKLIST.md** - Step-by-step checklist
- **CUSTOMIZATION_GUIDE.md** - How to customize

---

## 🎯 Project Structure

```
quiz_project/
├── quiz_project/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quiz_app/              # Main app
│   ├── migrations/
│   ├── templates/         # HTML files
│   ├── static/           # CSS files
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   └── urls.py
├── docs/                  # Documentation
├── manage.py
├── requirements.txt
└── db.sqlite3            # Database (created after migrate)
```

---

## ✨ Features

✅ Teacher - Create quizzes with MCQ
✅ Student - Take quizzes and get scores
✅ Admin - Manage all data
✅ SQLite Database
✅ Bootstrap 5 Design

---

**Everything is ready! Start with step 1 above.** 🎉
