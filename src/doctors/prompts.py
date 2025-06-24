from src.mcp_server import server

@server.prompt()
def get_doctor_prompt(name:str) -> str:
    """
    Prompt to get doctor information.
    """
    return "Please provide the doctor's name or ID to retrieve their information.\n\n you are looking for doctor: " + name