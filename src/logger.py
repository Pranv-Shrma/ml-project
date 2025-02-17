import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)




logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# This code configures the basic logging settings for the application
# - filename: Specifies the log file path where all logs will be stored
# - format: Defines the structure of log messages with:
#   - %(asctime)s: Timestamp of when the log was created
#   - %(lineno)d: Line number in code where log was generated
#   - %(name)s: Name of the logger (usually module name)
#   - %(levelname)s: Severity level of log (INFO, ERROR, etc)
#   - %(message)s: The actual log message
# - level: Sets minimum logging level to INFO, meaning it captures all info, warning, error and critical logs
#
# This logging configuration helps in debugging and monitoring the application by maintaining
# a detailed record of program execution and any issues that occur



# TESTING
# if __name__ == "__main__":
#     logging.info("Logging has started")

