from werkzeug.security import generate_password_hash

from app import app
from extensions import db
from models import Employee

with app.app_context():

    if Employee.query.count() == 0:

        admin = Employee(
            name="Admin",
            email="admin@gmail.com",
            password=generate_password_hash("admin123"),
            role="Admin",
            department="Management"
        )

        manager = Employee(
            name="Manager",
            email="manager@gmail.com",
            password=generate_password_hash("manager123"),
            role="Manager",
            department="IT"
        )

        employee = Employee(
            name="Employee",
            email="employee@gmail.com",
            password=generate_password_hash("employee123"),
            role="Employee",
            department="IT",
            manager_id=2
        )

        db.session.add(admin)
        db.session.add(manager)
        db.session.add(employee)

        db.session.commit()

        print("Sample users created successfully!")

    else:
        print("Employees already exist.")