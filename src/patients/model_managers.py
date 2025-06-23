from src.patients.models import PatientModel, CreatePatientArgs
from sqlalchemy.orm import Session
from typing import TypedDict
from src.logging import logger
from src.core.models import orm_object_to_query
from sqlalchemy import Date
from datetime import datetime

class GetAllPatientsQueryArg(TypedDict):
    name: str | None
    dob: datetime | None

class PatientModelManager:
    def __init__(self, session: Session):
        self.session = session

    def get_all_patients(self, query: GetAllPatientsQueryArg | None = None) -> list[PatientModel]:
        data  = self.session.query(PatientModel)
        if query:
            if query.get('name'):
                data = data.filter(PatientModel.name.ilike(f"%{query['name']}%"))
            if query.get('dob'):
                data = data.filter(PatientModel.dob == query['dob'])
        return data.all()


    @staticmethod
    def serialize_patients(patients: list[PatientModel]) -> list[dict]:
        return [patient.to_dict() for patient in patients]
