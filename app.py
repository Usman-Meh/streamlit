from flask import Flask, jsonify, request


app = Flask(__name__)



students = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 22},
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Student flask"})

@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify(students) 


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student['id'] == student_id:
            return jsonify(student)
    return jsonify({"error": "Student not found"})


@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_student = {
        "id": len(students) + 1,
        "name": data['name'],
        "age": data['age']
    }
    students.append(new_student)
    return jsonify(new_student), 201


if __name__ == '__main__':
    app.run(debug=True)