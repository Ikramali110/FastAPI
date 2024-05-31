from fastapi import APIRouter, Path, Query, Request
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List


from database import SessionLocal
from models import Student as DBStudent

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class OurBaseModel(BaseModel):
    class Config:
        from_attributes = True
class Student(OurBaseModel):
    id: int
    name: str
    city: str

class Studentcreate(OurBaseModel):
    name: str
    city: str

class Studentupdate(OurBaseModel):
    name: str
    city: str

class Studentdelete(OurBaseModel):
    name: str
    city: str

@router.get("/", response_model=List[Student], status_code=status.HTTP_200_OK)
def read_students(db: Session = Depends(get_db)):
    students = db.query(DBStudent).all()
    return [Student(id=student.id, name=student.name, city=student.city) for student in students]


@router.post("/create_student/", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: Studentcreate, db: Session = Depends(get_db)):
    # Create a new student instance
    new_student = DBStudent(name=student.name, city=student.city)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.put("/update_student/{student_id}", response_model=Student, status_code=status.HTTP_201_CREATED)
def update_student(student_id: int, student: Studentupdate, db: Session = Depends(get_db)):
    # Create a new student instance
    student_data = db.query(DBStudent).filter(DBStudent.id == student_id).first()
    student_data.name = student.name
    student_data.city = student.city
    db.commit()
    db.refresh(student_data)
    return student_data


@router.delete("/delete_student/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student_data = db.query(DBStudent).filter(DBStudent.id == student_id).first()

    db.delete(student_data)

    db.commit()
    return "student delete sucessfuly.."