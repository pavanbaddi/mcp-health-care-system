from sqlalchemy import Column, String
from src.core.models import BaseModel
from typing import TypedDict

class CreateDoctorArgs(TypedDict):
        name: str
        specialization: str

class DoctorModel(BaseModel):
    __tablename__ = 'doctors'

    name = Column(String(255), nullable=False)
    specialization = Column(String(255), nullable=False)