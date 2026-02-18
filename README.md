# 📔 Personal Diary Web Application

A beautiful and user-friendly Django web application for maintaining a personal diary with daily routines and thoughts.

## ✨ Features

- **User Authentication**: Secure registration and login system for each user
- **Personal Diary Entries**: Create, read, update, and delete your diary entries
- **Mood Tracking**: Record your mood for each entry with emojis
- **Search Functionality**: Search through your entries by title, content, or mood
- **Beautiful UI/UX**: Modern, responsive design with gradient backgrounds and smooth animations
- **Date Management**: Organize entries by date with calendar integration
- **Privacy**: Each user can only see and manage their own diary entries

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Navigate to the project directory**
   ```bash
   cd diary_project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your web browser and navigate to:
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📖 Usage Guide

### For New Users

1. **Register an Account**
   - Click on "Register here" from the login page
   - Fill in your username, email, and password
   - Click "Register" to create your account

2. **Login**
   - Enter your username and password
   - Click "Login" to access your diary

### Managing Diary Entries

1. **Create a New Entry**
   - Click the "New Entry" button in the navigation bar
   - Fill in the title, content, date, and optional mood
   - Click "Create Entry" to save

2. **View Your Entries**
   - Your diary entries are displayed on the home page
   - Entries show title, date, mood, and a preview of content
   - Click "View" to see the full entry

3. **Search Entries**
   - Use the search bar on the home page
   - Search by title, content, or mood
   - Results update automatically

4. **Edit an Entry**
   - Click "Edit" on any entry card
   - Modify the fields as needed
   - Click "Update Entry" to save changes

5. **Delete an Entry**
   - Click "Delete" on any entry card
   - Confirm the deletion when prompted
   - The entry will be permanently removed

## 🎨 UI Features

- **Responsive Design**: Works beautifully on desktop, tablet, and mobile devices
- **Color-coded Moods**: Visual emoji indicators for different moods
- **Smooth Animations**: Card hover effects and smooth transitions
- **Modern Gradient Background**: Eye-catching purple gradient design
- **Clean Typography**: Easy-to-read fonts with proper spacing
- **Intuitive Icons**: Font Awesome icons for better visual communication

## 🔒 Security Features

- Password validation and encryption
- CSRF protection on all forms
- User-specific data access (users can only see their own entries)
- Session-based authentication

## 📁 Project Structure

```
diary_project/
├── diary/                      # Main diary application
│   ├── migrations/            # Database migrations
│   ├── __init__.py
│   ├── admin.py              # Admin panel configuration
│   ├── apps.py               # App configuration
│   ├── forms.py              # Form definitions
│   ├── models.py             # Database models
│   ├── urls.py               # URL routing
│   └── views.py              # View functions
├── diary_project/            # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py
├── templates/               # HTML templates
│   └── diary/
│       ├── base.html        # Base template
│       ├── home.html        # Home page with entry list
│       ├── login.html       # Login page
│       ├── register.html    # Registration page
│       ├── entry_form.html  # Create/Edit entry form
│       ├── entry_detail.html # Full entry view
│       └── entry_confirm_delete.html # Delete confirmation
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🛠️ Customization

### Change Secret Key (Important for Production)

Edit `diary_project/settings.py` and change the `SECRET_KEY`:
```python
SECRET_KEY = 'your-new-secret-key-here'
```

### Modify Colors

The color scheme can be customized in the CSS variables in `templates/diary/base.html`:
```css
:root {
    --primary-color: #6366f1;
    --primary-dark: #4f46e5;
    --secondary-color: #8b5cf6;
    /* ... more colors */
}
```

### Add More Moods

Edit `diary/forms.py` in the `DiaryEntryForm` class to add more mood options:
```python
choices=[
    ('', 'Select mood (optional)'),
    ('happy', '😊 Happy'),
    # Add your custom moods here
]
```

## 🐛 Troubleshooting

### Port Already in Use
If port 8000 is already in use, run the server on a different port:
```bash
python manage.py runserver 8080
```

### Database Issues
If you encounter database errors, try:
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
Ensure the static files settings are correct in `settings.py` and run:
```bash
python manage.py collectstatic
```

## 📝 Development Notes

- The application uses SQLite database by default (stored in `db.sqlite3`)
- Debug mode is enabled by default (disable in production)
- For production deployment, update `settings.py`:
  - Set `DEBUG = False`
  - Update `ALLOWED_HOSTS`
  - Use a production-grade database (PostgreSQL, MySQL)
  - Set up proper static file serving

## 🤝 Contributing

Feel free to fork this project and customize it according to your needs!

## 📄 License

This project is open source and available for personal and educational use.

## 🎉 Enjoy Your Personal Diary!

Start capturing your thoughts, memories, and daily routines in style!
