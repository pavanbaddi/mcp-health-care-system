from src.mcp_server import server
from src.logging import logger
from src.settings import sql_session
from src.doctors.model_managers import DoctorModelManager, GetAllDoctorsQueryArg
from typing import TypedDict


@server.tool()
def doctors(name: str = '', specialization: str = '') -> list[dict[str, object]] | dict[str, str]:
    """
    This tool provides access to doctor records.
    Returns a list of all doctors in the system, including their names, specialties, and contact information.
    Each doctor is represented as a dictionary with the following keys:
    - `id`: Unique identifier for the doctor
    - `name`: Full name of the doctor
    - `specialization`: Medical specialty of the doctor
    - `created_at`: Datetime when the doctor record was created
    - `updated_at`: Datetime when the doctor record was last updated
    
    Args:
        name (str | None): Optional name filter for the doctors.
        specialization (str | None): Optional specialization filter for the doctors.
    """
    query: GetAllDoctorsQueryArg = {
        'name' : name,
        'specialization' : specialization,
    }
    result = DoctorModelManager(sql_session).get_all_doctors(query)
    
    if len(result) == 0:
        return {
            "message": "No doctors found matching the criteria."
        }
    
    doctors_list = DoctorModelManager.serialize_doctors(result)
    
    return doctors_list

