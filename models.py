from datetime import datetime
from flask_login import UserMixin

from extensions import db, login_manager


class Employee(UserMixin, db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(100), nullable=False)

    manager_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=True
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    reviews_received = db.relationship(
        "PerformanceReview",
        foreign_keys="PerformanceReview.employee_id",
        backref="employee",
        lazy=True
    )

    reviews_given = db.relationship(
        "PerformanceReview",
        foreign_keys="PerformanceReview.reviewed_by",
        backref="reviewer",
        lazy=True
    )


class PerformanceReview(db.Model):
    __tablename__ = "performance_reviews"

    review_id = db.Column(db.Integer, primary_key=True)

    review_title = db.Column(db.String(100), nullable=False)

    review_date = db.Column(db.Date, nullable=False)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    reviewed_by = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    review_period = db.Column(db.String(20), nullable=False)

    rating = db.Column(db.Integer, nullable=False)

    comments = db.Column(db.String(300))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))