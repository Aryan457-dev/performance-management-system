# Performance Management System

A role-based Performance Management System developed using **Flask**, **MySQL**, **SQLAlchemy**, **Bootstrap 5**, and **Flask-Login**. The application enables organizations to manage employee performance reviews through secure authentication, role-based dashboards, and review management features.

---

## 🚀 Live Demo

**Live Website:** https://performance-management-system-j57f.onrender.com

---

## 💻 GitHub Repository

**Repository:** https://github.com/Aryan457-dev/performance-management-system

---

## 📌 Features

### Authentication
- Secure Login & Logout
- Session Management
- Role-Based Authentication
- Protected Routes

### User Roles
- Admin
- Manager
- Employee

### Dashboard
- Personalized Dashboard
- User Information
- Role-Based Access
- Navigation Bar

### Performance Review Management
- Add Performance Review
- Edit Performance Review
- Delete Performance Review
- View Review List
- Employee Selection
- Review Comments
- Rating (1–10)
- Review Period (Monthly, Quarterly, Annual)

### Filters
- Search Employee
- Filter by Review Period
- Filter by Rating
- Filter by Date Range

### Statistics
- Total Reviews
- Monthly Reviews
- Quarterly Reviews
- Annual Reviews

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask SQLAlchemy
- Flask Login
- Flask Migrate

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- Jinja2

### Database
- MySQL (Development)
- PostgreSQL (Production)

### Deployment
- Render
- Gunicorn

---

## 📂 Project Structure

```
Performance-Management-System/
│
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   └── review.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add_review.html
│   ├── edit_review.html
│   ├── review_list.html
│   └── review_details.html
│
├── static/
│   └── css/
│       └── style.css
│
├── migrations/
├── app.py
├── config.py
├── extensions.py
├── models.py
├── seed.py
├── requirements.txt
├── Procfile
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Aryan457-dev/performance-management-system.git
```

```bash
cd performance-management-system
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Configuration

Create a MySQL database named:

```sql
performance_management
```

Update the database connection inside `config.py`.

Run migrations:

```bash
flask db init
flask db migrate -m "Initial Migration"
flask db upgrade
```

(Optional)

```bash
python seed.py
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🔐 Default Login

### Admin

```
Email:
admin@gmail.com

Password:
admin123
```

---

## 📸 Main Modules

- Login
- Dashboard
- Add Review
- Edit Review
- Delete Review
- View Reviews
- Search Reviews
- Review Statistics

---

## 📈 Future Enhancements

- Email Notifications
- PDF Report Generation
- Performance Graphs
- Employee Self-Appraisal
- Pagination
- Export to Excel
- Department Management

---

## 👨‍💻 Developed By

**Aryan Dabholkar**

GitHub: https://github.com/Aryan457-dev

---

## 📄 License

This project is developed for educational and internship purposes.
