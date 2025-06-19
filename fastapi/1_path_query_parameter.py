from fastapi import FastAPI, Path ,HTTPException
import json
import uvicorn

app = FastAPI()

def read_std():
    """Read all std data from the JSON file"""
    with open('std.json', 'r') as file:
        data = json.load(file)
    return data['std']

def get_student_by_id(student_id: int):
    """Get a specific student by ID"""
    std = read_std()
    for student in std:
        if student['id'] == student_id:
            return student
    return None

@app.get('/')
def read_root():
    return {'message': 'Hello, World!'}

@app.get('/std')
def view_all_std():
    """Get all std"""
    return {'std': read_std()}

@app.get('/std/{student_id}')
def view_student(student_id: int=Path(...,title="The ID of the student in the db", exmple="1")):
    """Get a specific student by ID"""
    student = get_student_by_id(student_id)
    if student:
        return student

    raise HTTPException(status_code=404, detail="Student not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
