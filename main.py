from fastapi import FastAPI, status, HTTPException

app = FastAPI()

students = {}
studentID = 0


@app.get("/")
def home():
    return {"Welcome To Student FastAPI Application"}

# creating a student
@app.post("/student")
def student_create(name: str,age: int,sex: str,height: float):
    student_data = {"Id" : 0,"Name" : "", "Age" : "", "Sex":"", "height": 0.0}
    
    global studentID
    studentID += 1

    student_data["Id"] = studentID
    student_data["Name"] = name
    student_data["Age"] = age
    student_data["Sex"] = sex
    student_data["height"] = height

    students[student_data["Id"]] = student_data

    return student_data

# Get all student
@app.get("/student")
def student():
    return students
    
# Get A Single Student information
@app.get("/student/{student_id}")
def student_get(student_id: int):
    student = students.get(student_id)
    if student_id in students:
        return student
    raise HTTPException(status_code=400, detail="Student not found")

# Updating Student record
@app.put("/student/{student_Id}")
def student_update(student_Id: int,name: str,age: int,sex: str,height: float):
    student_data = {"Id" : 0,"Name" : "", "Age" : "", "Sex":"", "height": 0.0}
    student = students.get(student_Id)
    if student_Id in students:
        student_data["Id"] = studentID
        student_data["Name"] = name
        student_data["Age"] = age
        student_data["Sex"] = sex
        student_data["height"] = height
        students[student_Id] = student_data
        
        return Response(message="Student updated successfully", data=student_data)
        
    raise HTTPException(status_code=400, detail="Student not found")

# Delete a student
@app.delete("/student/{student_Id}")
def delete_student(student_Id:int):
    student = students.get(student_Id)
    if student_Id in students:
        del students[student_Id]
        return ("Student Deleted Successfully")
    raise HTTPException(status_code=400, detail="Student not found")





