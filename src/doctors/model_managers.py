from src.doctors.models import DoctorModel, CreateDoctorArgs
from sqlalchemy.orm import Session
from typing import TypedDict
from src.logging import logger

class GetAllDoctorsQueryArg(TypedDict):
    name: str | None
    specialization: str | None

class DoctorModelManager:
    def __init__(self, session: Session):
        self.session = session

    def get_all_doctors(self, query: GetAllDoctorsQueryArg | None = None) -> list[DoctorModel]:
        data  = self.session.query(DoctorModel)
        
        if query:
            if query.get('name'):
                logger.info(f"Filtering doctors by name: {query['name']}")
                data = data.filter(DoctorModel.name.ilike(f"%{query['name']}%"))
            if query.get('specialization'):
                data = data.filter(DoctorModel.specialization.ilike(f"%{query['specialization']}%"))
                
        return data.all()

    def get_doctor_by_id(self, doctor_id):
        return self.session.query(DoctorModel).filter(DoctorModel.id == doctor_id).first()

    def create_doctor(self, doctor_data: CreateDoctorArgs) -> DoctorModel:
        new_doctor = DoctorModel(**doctor_data)
        self.session.add(new_doctor)
        self.session.commit()
        return new_doctor

    def update_doctor(self, doctor_id, doctor_data: CreateDoctorArgs):
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            for key, value in doctor_data.items():
                setattr(doctor, key, value)
            self.session.commit()
        return doctor

    def delete_doctor(self, doctor_id):
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            self.session.delete(doctor)
            self.session.commit()
        return doctor

    @staticmethod
    def serialize_doctors(doctors: list[DoctorModel]) -> list[dict]:
        return [doctor.to_dict() for doctor in doctors]
