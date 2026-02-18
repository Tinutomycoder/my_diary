# 🚀 Quick Start Guide

## Setup in 5 Minutes

### 1. Open Terminal in Project Directory
```bash
cd diary_project
```

### 2. Create Virtual Environment (Windows)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Django
```bash
pip install -r requirements.txt
```

### 4. Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server
```bash
python manage.py runserver
```

### 6. Open Browser
Go to: http://127.0.0.1:8000/

### 7. Register Your Account
- Click "Register here"
- Create your username and password
- Start writing your diary!

## That's It! 🎉

Your personal diary is ready to use!

## Optional: Create Admin Account
```bash
python manage.py createsuperuser
```
Access admin at: http://127.0.0.1:8000/admin/
