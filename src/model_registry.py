from src.patients.models import PatientModel
from src.doctors.models import DoctorModel
import src.doctors.tools
import src.patients.tools

MODELS_REGISTRY = [PatientModel, DoctorModel]

TOOLS_REGISTRY = [
    'doctors.tools',
]


