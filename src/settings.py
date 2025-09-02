from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
import os
from src.core.imports import load_module
from pathlib import Path

SRC_DIR = Path().resolve()

INSTALLED_APPS = [
    'doctors',
    'patients',
]

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

def load_modules():
    for app_name in INSTALLED_APPS:

        filepath = os.path.join(SRC_DIR, app_name, 'models.py')

        module_file_exists = os.path.isfile(filepath)

        if module_file_exists:
            load_module(app_name, filepath)
