import logging
import os
import sys
from typing import Optional


class ColoredFormatter(logging.Formatter):
    """Custom formatter to add colors to log levels."""
    
    COLORS = {
        "DEBUG": "\033[36m",     # Cyan
        "INFO": "\033[32m",      # Green
        "WARNING": "\033[33m",   # Yellow
        "ERROR": "\033[31m",     # Red
        "CRITICAL": "\033[35m",  # Magenta
    }
    RESET = "\033[0m"
    
    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        record.levelname = f"{log_color}{record.levelname}{self.RESET}"
        return super().format(record)


def create_logger(name: str, level: Optional[str] = None, file: Optional[str] = None) -> logging.Logger:
    """
    Create a logger with colorized console output and optional file output.
    
    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL). 
               Defaults to DEBUG or value from LOG_LEVEL environment variable
        file: Optional file path to write logs to. 
               Defaults to None or value from LOG_FILE environment variable
        
    Returns:
        Configured logger instance
    """
    # Get level from environment or use provided level or default to DEBUG
    if level is None:
        level = os.getenv("LOG_LEVEL", "DEBUG")
    
    # Get file from environment if not provided
    if file is None:
        file = os.getenv("LOG_FILE")
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Console handler with colors
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, level.upper()))
    
    # Format with timestamp, logger name, level, and message
    console_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    console_formatter = ColoredFormatter(console_format, datefmt="%Y-%m-%d %H:%M:%S")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # File handler if specified
    if file:
        file_handler = logging.FileHandler(file)
        file_handler.setLevel(getattr(logging, level.upper()))
        
        # File format (without colors)
        file_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        file_formatter = logging.Formatter(file_format, datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    
    return logger