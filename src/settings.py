import src.logging
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
import os
# 1. Define the database engine
# Replace with your MySQL connection details
connection_string = os.getenv("CONNECTION_STRING")
if connection_string is None:
    raise ValueError("CONNECTION_STRING environment variable is not set.")

engine = create_engine(connection_string)
sql_session = Session(engine)

# 2. Define a base class for declarative models
Base = declarative_base()

def on_boot():
    Base.metadata.create_all(engine)