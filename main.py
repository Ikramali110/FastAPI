from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import routers.Routes
from routers import Routes

import models
from database import SessionLocal
from models import Student as DBStudent
app = FastAPI()

app.include_router(routers.Routes.router)


# Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# class OurBaseModel(BaseModel):
#     class Config:
#         from_attributes = True
# class Student(OurBaseModel):
#     id: int
#     name: str
#     city: str
#
# class Studentcreate(OurBaseModel):
#     name: str
#     city: str
#
# class Studentupdate(OurBaseModel):
#     name: str
#     city: str
#
# class Studentdelete(OurBaseModel):
#     name: str
#     city: str



