from dotenv import load_dotenv
load_dotenv()
import src.model_registry
from src.mcp_server import server

if __name__ == "__main__":
    from src.settings import on_boot
    on_boot()
    server.run()
