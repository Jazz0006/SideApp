import unittest
from main import create_app
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["FLASK_ENV"] = "testing"

class TestCourses(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_course_index(self):
        response = self.client.get("/courses/")
        #data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Course Index</h1>', response.data)

    def test_create_bad_course(self):
        response = self.client.post("/courses/", data = {"course_name": ""})
        self.assertEqual(response.status_code, 400)