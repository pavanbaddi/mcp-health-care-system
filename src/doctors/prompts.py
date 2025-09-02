from src.mcp_server import server
from src.doctors.model_managers import DoctorModelManager, GetAllDoctorsQueryArg, CreateDoctorArgs
from src.logging import app_logger
from src.settings import sql_session
from src.doctors.models import DoctorModel
from mcp.server.fastmcp.exceptions import FastMCPError

doctor_model_manager = DoctorModelManager(session=sql_session)

@server.prompt(
    name="get_doctor_prompt",
    description="Using this prompt you can get doctor information."
)
def get_doctor_prompt(name:str) -> str:
    query: GetAllDoctorsQueryArg = {
        "name": name
    }
    doctors = doctor_model_manager.get_all_doctors(query=query)

    if len(doctors) == 0:
        return f"No doctors matching for doctor name {name}"
    
    if len(doctors) > 1:
        formatted_doctors = format_doctors(doctors=doctors)
        return f"""There many doctors matching with name **{name}**\n
        {formatted_doctors}
        """

    formatted_doctor = format_doctors(doctors=doctors)
    return f"""Details of doctor **{doctors[0].name}**\n
    {formatted_doctor}
    """


@server.prompt(
    name="create_doctor_prompt",
    description="Using this prompt you can create new doctor."
)
def create_doctor_prompt(name:str, specialization: str) -> str:
    query: CreateDoctorArgs = {
        "name": name,
        "specialization": specialization
    }
    doctor = doctor_model_manager.create_doctor(doctor_data=query)

    if not doctor:
        return FastMCPError(f"Unable to create doctor with name: {name}")
    
    return f"""New doctor with name {doctor.name} successfully created
    """


def format_doctors(doctors: list[DoctorModel] | DoctorModel):

    if isinstance(doctors, list):
        mapped_str = list(map(format_doctor, doctors))
        
        return "\n".join(mapped_str)
    
    return format_doctor(doctor=doctors)
        
def format_doctor(doctor: DoctorModel) -> str:
    return f"""
    {doctor.name} (Specialization: {doctor.specialization})
    """

