import fastapi
from student_data import students

app = fastapi.FastAPI()


# method for welcome message for the api at the root
@app.get("/")
async def welcome():
    return "Welcome to the student api using python"


# method to get all the student data
@app.get("/students")
async def get_students():
    return students


# method to get student data by student id
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise fastapi.HTTPException(status_code=404, detail="student not found")


# method to add student data
@app.post("/students")
async def add_student(student: dict):
    students.append(student)
    return students


# method to update student data
@app.put("/students/{student_id}")
async def update_student(student_id: int, student: dict):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = student
            return students
    raise fastapi.HTTPException(status_code=404, detail="student not found")


# method to delete student data
@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            del students[index]
            return students
    raise fastapi.HTTPException(status_code=404, detail="student not found")

# uvicorn command to run the app on port 8000
# uvicorn main:app --reload --port 8080
# command to create requirements.txt file
# pip freeze > requirements.txt
