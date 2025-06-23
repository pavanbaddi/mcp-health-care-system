from src.mcp_server import server
from src.logging import logger
from src.settings import sql_session
from src.patients.model_managers import PatientModelManager, GetAllPatientsQueryArg
from typing import TypedDict
from datetime import datetime, date


@server.tool()
def patients(name: str = '', dob: str = '') -> list[dict[str, object]] | dict[str, str]:
    """
    This tool provides access to patient records.
    Returns a list of all patients in the system, including their names and dates of birth.
    Each patient is represented as a dictionary with the following keys:
    - `id`: Unique identifier for the patient
    - `name`: Full name of the patient
    - `dob`: Date of birth of the patient
    - `created_at`: Datetime when the patient record was created
    - `updated_at`: Datetime when the patient record was last updated
    """
    query: GetAllPatientsQueryArg = {
        'name' : name,
        'dob' : datetime.strptime(dob, "%Y-%m-%d") if dob else None,
    }
    result = PatientModelManager(sql_session).get_all_patients(query)
    
    if len(result) == 0:
        return {
            "message": "No patients found matching the criteria."
        }
    
    patients_list = PatientModelManager.serialize_patients(result)
    
    return patients_list

