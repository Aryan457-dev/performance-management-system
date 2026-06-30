from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from extensions import db
from models import Employee, PerformanceReview

review_bp = Blueprint("review", __name__)


@review_bp.route("/reviews")
@login_required
def review_list():

    if current_user.role == "Admin":
        query = PerformanceReview.query

    elif current_user.role == "Manager":

        team_ids = [
            emp.id
            for emp in Employee.query.filter_by(manager_id=current_user.id).all()
        ]

        query = PerformanceReview.query.filter(
            PerformanceReview.employee_id.in_(team_ids)
        )

    else:

        query = PerformanceReview.query.filter_by(
            employee_id=current_user.id
        )

    # ---------------- Filters ---------------- #

    search = request.args.get("search")
    period = request.args.get("period")
    rating = request.args.get("rating")
    from_date = request.args.get("from_date")
    to_date = request.args.get("to_date")

    if search:

        query = query.join(Employee).filter(
            Employee.name.ilike(f"%{search}%")
        )

    if period:
        query = query.filter(
            PerformanceReview.review_period == period
        )

    if rating:
        query = query.filter(
            PerformanceReview.rating == int(rating)
        )

    if from_date:
        query = query.filter(
            PerformanceReview.review_date >= from_date
        )

    if to_date:
        query = query.filter(
            PerformanceReview.review_date <= to_date
        )

    reviews = query.order_by(
        PerformanceReview.review_date.desc()
    ).all()

    return render_template(
        "review_list.html",
        reviews=reviews
    )

@review_bp.route("/reviews/add", methods=["GET", "POST"])
@login_required
def add_review():

    if current_user.role == "Employee":
        flash("You are not authorized to add reviews.", "danger")
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":

        review = PerformanceReview(
            review_title=request.form["review_title"],
            employee_id=request.form["employee_id"],
            reviewed_by=current_user.id,
            review_date=request.form["review_date"],
            review_period=request.form["review_period"],
            rating=request.form["rating"],
            comments=request.form["comments"]
        )

        db.session.add(review)
        db.session.commit()

        flash("Review Added Successfully!", "success")

        return redirect(url_for("review.review_list"))

    if current_user.role == "Admin":

        employees = Employee.query.filter(
            Employee.id != current_user.id
        ).all()

    else:   # Manager

        employees = Employee.query.filter_by(
            manager_id=current_user.id
        ).all()

    return render_template(
        "add_review.html",
        employees=employees
    )


@review_bp.route("/reviews/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_review(id):

    review = PerformanceReview.query.get_or_404(id)

    if request.method == "POST":

        review.review_title = request.form["review_title"]
        review.employee_id = request.form["employee_id"]
        review.review_date = request.form["review_date"]
        review.review_period = request.form["review_period"]
        review.rating = request.form["rating"]
        review.comments = request.form["comments"]

        db.session.commit()

        flash("Review Updated Successfully!", "success")

        return redirect(url_for("review.review_list"))

    employees = Employee.query.all()

    return render_template(
        "edit_review.html",
        review=review,
        employees=employees
    )


@review_bp.route("/reviews/delete/<int:id>")
@login_required
def delete_review(id):

    review = PerformanceReview.query.get_or_404(id)

    db.session.delete(review)
    db.session.commit()

    flash("Review Deleted Successfully!", "success")

    return redirect(url_for("review.review_list"))