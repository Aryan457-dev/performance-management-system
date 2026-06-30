from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from models import Employee

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        employee = Employee.query.filter_by(email=email).first()

        if employee and check_password_hash(employee.password, password):
            login_user(employee)
            flash("Login Successful!", "success")
            return redirect(url_for("dashboard.dashboard"))

        flash("Invalid Email or Password", "danger")

    return render_template("login.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged Out Successfully!", "success")
    return redirect(url_for("auth.login"))