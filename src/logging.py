import logging
from logging.handlers import TimedRotatingFileHandler
import os

# Define the log directory
log_directory = "logs"

# Create the log directory if it doesn't exist
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Create a TimedRotatingFileHandler
log_handler = TimedRotatingFileHandler(
    f"{log_directory}/app.log",  # Log file name
    when="midnight",  # Rotate logs at midnight
    interval=1,  # Interval in days
    backupCount=30,  # Keep the last 7 log files
)

# Set the logging level
log_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter("[%(asctime)s][%(levelname)s]- %(message)s")
log_handler.setFormatter(formatter)    

# Create a logger and add the handler to it    
app_logger = logging.getLogger(__name__)
app_logger.addHandler(log_handler)
app_logger.setLevel(logging.DEBUG)