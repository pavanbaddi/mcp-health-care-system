from mcp.server.fastmcp import FastMCP

instructions = """
You are a healthcare system that manages patient and doctor records.
You will receive requests to create, read, update, and delete patient and doctor information.
Your responses should be in a structured format, and you should ensure data integrity and security.
"""

settings = {
    "debug": True,
    "log_level": 'CRITICAL',
}

server = FastMCP("HealthCareSystem", instructions=instructions, settings=settings)