"""
Utility functions for validation and security
"""
import hashlib
import re

def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password, stored_hash):
    """Verify if input password matches stored hash"""
    return hash_password(input_password) == stored_hash

def validate_phone(phone):
    """Validate phone number"""
    return len(phone) >= 10 and phone.isdigit()

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_price(price):
    """Validate price is positive"""
    try:
        return float(price) > 0
    except ValueError:
        return False

def validate_quantity(quantity):
    """Validate quantity is positive integer"""
    try:
        return int(quantity) > 0
    except ValueError:
        return False

def get_positive_int(prompt, error_msg="Please enter a valid positive number!"):
    """Get positive integer from user input"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print(f"Must be positive! {error_msg}")
        except ValueError:
            print(error_msg)

def get_positive_float(prompt, error_msg="Please enter a valid positive number!"):
    """Get positive float from user input"""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print(f"Must be positive! {error_msg}")
        except ValueError:
            print(error_msg)
