from src.patients.model import PatientModel
from src.doctors.models import DoctorModel
import src.doctors.tools

MODELS_REGISTRY = [PatientModel, DoctorModel]

TOOLS_REGISTRY = [
    'doctors.tools',
]


