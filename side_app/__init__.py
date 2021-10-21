from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world! Check this out!"

@app.route('/students/')
def get_students():
    return "This is all students..."

@app.route('/students/<int:student_id>')
def get_specific_students(student_id):
    return f"This is a apge displaying information about student {student_id}."

if __name__ == '__main__':
    app.run(debug=True)