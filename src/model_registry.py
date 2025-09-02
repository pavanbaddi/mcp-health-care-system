from src.patients.models import PatientModel
from src.doctors.models import DoctorModel
import src.doctors.tools
import src.doctors.prompts
import src.patients.tools
import src.patients.prompts

MODELS_REGISTRY = [PatientModel, DoctorModel]

TOOLS_REGISTRY = [
    'doctors.tools',
]