import logging
from logging.handlers import RotatingFileHandler
import os

# Configure the handler to rotate at 1MB, keeping 3 backups
log_file = "app.log"
handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=3) #keep 3 old log files with 1 MB limit
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger = logging.getLogger("MyLogger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Example logging
for i in range(10000):
    logger.info(f"Log message {i}")
