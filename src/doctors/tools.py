from src.mcp_server import server
from src.logging import logger
from src.settings import sql_session
from src.doctors.model_managers import DoctorModelManager

@server.tool()
def doctors() -> list[dict[str, object]]:
    """This tool provides access to doctor records."""
    result = DoctorModelManager(sql_session).get_all_doctors()
    doctors_list = DoctorModelManager.serialize_doctors(result)
    
    return doctors_list