# 🎓 EduLearn LMS – Learning Management System

## 📌 Project Overview

EduLearn LMS is a full-stack web application built using Django that allows instructors to create and manage courses, students to enroll and learn, and admins to monitor the platform. It includes role-based authentication and a modern responsive UI.

---

## 🚀 Features

### 👑 Admin

* View total students and instructors
* View all courses created by instructors
* Profile management
* Login / Logout
* Modern dashboard with sidebar and footer

---

### 🎓 Instructor

* Dashboard to view own courses
* Create new courses
* Edit and delete courses
* Profile page
* Login / Logout
* Sidebar with collapse functionality
* Modern UI with navbar and footer

---

### 🎒 Student

* View all available courses
* Enroll in courses
* View enrolled courses
* Profile page
* Login / Logout
* Clean dashboard with modern UI

---

## 🧑‍💻 Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap, Tailwind CSS
* **Database:** SQLite
* **Authentication:** Django Auth System
* **Deployment:** Render

---

## 📂 Project Structure

```
lms_project/
│
├── accounts/        # User authentication and roles
├── courses/         # Course management and enrollment
├── dashboard/       # Role-based dashboards
├── templates/       # HTML templates
├── static/          # Static files (CSS, JS)
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation (Local Setup)

1. Clone the repository

```
git clone https://github.com/yourusername/lms-project.git
cd lms-project
```

2. Install dependencies

```
python -m pip install -r requirements.txt
```

3. Run migrations

```
python manage.py migrate
```

4. Create superuser

```
python manage.py createsuperuser
```

5. Run server

```
python manage.py runserver
```

---

## 🌐 Deployment

This project is deployed using **Render** with:

* Gunicorn for production server
* WhiteNoise for static files

---

## 🔐 Authentication

* Role-based access (Admin, Instructor, Student)
* Login required to access dashboard
* Secure routing using Django decorators

---

## 🎯 Project Objective

To build a role-based Learning Management System where:

* Instructors create courses
* Students enroll and learn
* Admin monitors the system

---

## 🏆 Conclusion

This project demonstrates full-stack development using Django with clean UI, role-based access, and real-world functionality suitable for academic submission and portfolio use.

---

## 📧 Contact

Developed by: **Sudeep Singh Jadoun**
