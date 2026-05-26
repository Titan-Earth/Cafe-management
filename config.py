"""
Configuration and constants for Cafe Management System
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Database Configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "cafe")
}

# Application Constants
MIN_PHONE_LENGTH = 10
MIN_PASSWORD_LENGTH = 6
