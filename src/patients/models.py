from sqlalchemy import Date, Column, String
from src.core.models import BaseModel
import uuid
from sqlalchemy.sql import func
from sqlalchemy import DateTime
from typing import TypedDict

class CreatePatientArgs(TypedDict):
        id: str
        name: str
        dob: Date

class PatientModel(BaseModel):
    __tablename__ = 'patients'

    id = Column(String(255), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    dob = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now(), nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)