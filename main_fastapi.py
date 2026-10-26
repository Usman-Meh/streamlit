from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


app = FastAPI(title="Student API", version="1.0")


 # Same in-memory list as Flask example
students = [
 {"id": 1, "name": "Ali", "grade": "A"},
 {"id": 2, "name": "Sara", "grade": "B"},
 ]


class StudentCreate(BaseModel):
    name: str
    grade: Optional[str] = None




@app.get("/")
async def read_root():
    return {"message": "Welcome to the Student Fast API"}

@app.get("/students")
async def get_all_students():
    return students

@app.post("/students" , status_code=201)
async def add_student(student: StudentCreate):
    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "grade": student.grade
    }
    students.append(new_student)
    return new_student


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for student in students:
        if student['id'] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")



@app.put("/students/{student_id}")
async def update_student(student_id: int, student: StudentCreate):
    for s in students:
        if s['id'] == student_id:
            s['name'] = student.name
            s['grade'] = student.grade
            return s
    raise HTTPException(status_code=404, detail="Student not found")
    

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for s in students:
        if s['id'] == student_id:
            students.remove(s)
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")