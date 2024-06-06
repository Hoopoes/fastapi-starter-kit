import os
import logging
from config import Config
from datetime import datetime
from logging.config import dictConfig

# Ensure logs directory exists
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Logging configuration
log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s | %(asctime)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "file": {
            "formatter": "default",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(log_dir, f"{current_date}.log"),
            "when": "midnight",
            "backupCount": 7,
            "encoding": "utf-8",
        },
    },
    "loggers": {
        f"{Config.app_name}": {
            "handlers": ["default", "file"],
            "level": "DEBUG",  # Set your desired logging level here
        },
    },
}

# Configure logging
dictConfig(log_config)

# Define a logger
log = logging.getLogger(Config.app_name)

# Test logging
log.info(f"{Config.app_name} logger initialized")