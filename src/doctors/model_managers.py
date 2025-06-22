from src.doctors.models import DoctorModel, CreateDoctorArgs
from sqlalchemy.orm import Session

class DoctorModelManager:
    def __init__(self, session: Session):
        self.session = session

    def get_all_doctors(self):
        return self.session.query(DoctorModel).all()

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
