from operator import countOf
import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

def create_app():

    app = Flask(__name__)
    app.config.from_object("config.app_config")

    db = SQLAlchemy(app)

    class Course(db.Model):
        __tablename__ = "courses"
        course_id = db.Column(db.Integer, primary_key = True)
        course_name = db.Column(db.String(80), unique = True, nullable = False)

        def __init__(self, course_name):
            self.course_name = course_name

        @property
        def serialize(self):
            return {
                "course_id": self.course_id,
                "course_name": self.course_name
            }

    db.create_all()

    @app.route('/')
    def homepage():
        return "Hello, world! Check this out!"

    @app.route("/courses/", methods = ["GET"])
    def get_courses():
        courses = Course.query.all()
        return jsonify([course.serialize for course in courses])

    @app.route('/students/')
    def get_students():
        return "This is all students..."

    @app.route('/students/<int:student_id>')
    def get_specific_students(student_id):
        return f"This is a apge displaying information about student {student_id}."

    return app
    #app.run(debug=True)