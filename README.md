
# Android App Task Management Platform

## Overview
This project is a task management platform that enables administrators to manage Android apps and assign points for users to earn by completing tasks. Users can upload screenshots as proof of task completion and track their points. The platform consists of two main sections: Admin-facing and User-facing functionalities.

---

## Features

### Admin-Facing Features
1. **Admin Login**: Secure login for administrators (not using the default Django admin).
2. **Add Apps**: Admins can add Android apps with details such as:
   - App Name
   - App Link
   - Category/Sub-category
   - Points for task completion
   - App Icon
3. **Manage Apps**: View and edit the list of apps added to the platform.

### User-Facing Features
1. **User Signup and Login**: Secure user authentication system.
2. **Profile Management**: Users can view and update their profile details, including:
   - First Name
   - Last Name
   - Username
   - Email
   - Change Password functionality
3. **Task Dashboard**:
   - View a list of apps with their associated points.
   - Drag-and-drop or upload a screenshot to confirm task completion.
4. **Points Tracking**:
   - Display points earned for completed tasks.
   - Sidebar dynamically updates with points earned.

---

## Tech Stack
- **Backend**: Django Framework
- **Frontend**: HTML, CSS, JavaScript 
- **Database**: SQLite 
- **Authentication**: Django's built-in authentication system

---

## Installation

### Prerequisites
1. Python 3.8+
2. pip (Python package installer)

### Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the application at `http://127.0.0.1:8000/`.

---

## Folder Structure
- **app/**
  - `models.py`: Contains database models (e.g., User, App, Screenshot).
  - `views.py`: Contains all the view logic for handling user and admin functionalities.
  - `urls.py`: Routes requests to the appropriate views.
  - `forms.py`: Contains form classes for the admin dashboard and other forms.
  - `templates/`: Contains all HTML files.
- **media/**
  - saves the app_icon and screenshot uploaded by user

---

## Database Schema

### Models
1. **User**
   - First Name
   - Last Name
   - Username
   - Email
   - Password

2. **App**
   - Name
   - Link
   - Category
   - Sub-category
   - Points
   - Icon

3. **Screenshot**
   - App (Foreign Key)
   - Image (FileField)

---

## API Endpoints
- `/api/apps/`: Get the list of apps.
- `/api/user/<id>/`: Get details of a specific user.

---

## Usage
1. Admin logs in and adds apps via the custom admin dashboard.
2. Users sign up, log in, and view available apps.
3. Users upload screenshots to confirm task completion and earn points.
4. Points are updated in real-time in the sidebar.


