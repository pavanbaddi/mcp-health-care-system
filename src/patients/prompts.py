from src.mcp_server import server
from src.patients.model_managers import PatientModelManager, GetAllPatientsQueryArg
from src.logging import app_logger
from src.settings import sql_session
from src.patients.models import PatientModel, CreatePatientArgs
from mcp.server.fastmcp.exceptions import FastMCPError
from datetime import date

patient_model_manager = PatientModelManager(session=sql_session)

@server.prompt(
    name="get_patient_prompt",
    description="Using this prompt you can get patient information."
)
def get_patient_prompt(name:str) -> str:
    query: GetAllPatientsQueryArg = {
        "name": name
    }
    patients = patient_model_manager.get_all_patients(query=query)

    if len(patients) == 0:
        return f"No patients matching for name {name}"
    
    if len(patients) > 1:
        formatted_patient = format_patients(patients=patients)
        return f"""There many patients matching with name **{name}**\n
        {formatted_patient}
        """

    formatted_patient = format_patients(patients=patients)
    return f"""Details of patient **{patients[0].name}**\n
    {formatted_patient}
    """


@server.prompt(
    name="create_patient_prompt",
    description="Using this prompt you can create new patient."
)
def create_patient_prompt(name:str, dob: date) -> str:
    query: CreatePatientArgs = {
        "name": name,
        "dob": dob
    }
    patient = patient_model_manager.create_patient(query=query)

    if not patient:
        return FastMCPError(f"Unable to create patient with name: {name}")
    
    return f"""New patient with name {patient.name} successfully created
    """


def format_patients(patients: list[PatientModel] | PatientModel):

    if isinstance(patients, list):
        mapped_str = list(map(format_patient, patients))
        
        return "\n".join(mapped_str)
    
    return format_patient(patient=patients)
        
def format_patient(patient: PatientModel) -> str:
    return f"""
    {patient.name} (Date of birth: {patient.dob})
    """

