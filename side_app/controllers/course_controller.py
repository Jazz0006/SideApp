from flask import Blueprint, jsonify, request, render_template
from main import db
from models.courses import Course
from schemas.courses_schema import courses_schema, course_schema

courses = Blueprint('courses', __name__)

@courses.route('/')
def homepage():
    return "Hello, world! Check this out!"

@courses.route("/courses/", methods=["GET"])
def get_courses():
    data = {
        "page_title": "Course Index",
        "courses": courses_schema.dump(Course.query.all())
    }
    return render_template("course_index.html", page_data = data)
    #courses = Course.query.all()
    #return jsonify(courses_schema.dump(courses))

@courses.route("/courses/", methods=["POST"])
def create_course():
    new_course = course_schema.load(request.form)
    print(new_course)
    db.session.add(new_course)
    db.session.commit()
    return jsonify(course_schema.dump(new_course))

@courses.route("/courses/<int:id>/", methods = ["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course_schema.dump(course))

@courses.route("/courses/<int:id>/", methods=["PUT", "PATCH"])
def update_course(id):
    course = Course.query.filter_by(course_id=id)
    updated_fields = course_schema.dump(request.json)
    if updated_fields:
        course.update(updated_fields)
        db.session.commit()
    return jsonify(course_schema.dump(course.first()))

@courses.route("/courses/<int:id>/", methods = ["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify(course_schema.dump(course))