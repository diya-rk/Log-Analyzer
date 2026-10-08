import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_time(login_time):
    pattern = r'^([01][0-9]|2[0-3]):[0-5][0-9]$'
    return re.match(pattern, login_time) is not None

def validate_record(record):
    parts = record.split()
    if len(parts) != 3:
        return False
    username, email, login_time = parts
    return validate_email(email) and validate_time(login_time)