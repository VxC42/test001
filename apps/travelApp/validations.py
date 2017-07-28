import re
from .models import User, Trip
from datetime import datetime


NAME = re.compile(r'^[a-zA-z ]+$')
USERNAME = re.compile(r'^[a-zA-z0-9_]+$')
PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

def validReg(user):
    error=[]
    isValid=True

    if len(user['name'])<3:
        isValid=False
        error.append("Name must consist of at least 3 characters")
    if not re.match(NAME, user['name']):
        isValid=False
        error.append("Name must only be letters")
    if len(user['username'])<3:
        isValid=False
        error.append("Name must consist of at least 3 characters")
    if not re.match(USERNAME, user['username']):
        isValid=False
        error.append("Username can only contain letters, numbers or underscore(_)")
    if len(user['password'])<8:
        isValid=False
        error.append("Password must be more than 8 characters")
    if user['password'] != user['confirm_password']:
        isValid=False
        error.append("Passwords do not match")

    return {"isValid":isValid, "errors":error}

def validLogin(user):
    error=[]
    isValid=True

    if not re.match(USERNAME, user['username']):
        isValid=False
        error.append("Email is not in database")
    if len(user['password'])<8:
        isValid=False
        error.append("Password does not match Email info")

    return {"isValid":isValid, "errors":error}

def validForm(plan):
    error=[]
    isValid=True
    today = str(datetime.today().strftime("%Y-%m-%d "))
    string = datetime.today().strptime(today, "%Y-%m-%d ")
    startDate = datetime.strptime(plan['startDate'],"%Y-%m-%d")
    endDate = datetime.strptime(plan['endDate'],"%Y-%m-%d")

    if len(plan['destination'])==0:
        isValid=False
        error.append("Please enter a destination.")
    if len(plan['description'])==0:
        isValid=False
        error.append("Please enter a description.")
    if len(plan['startDate'])==0:
        isValid=False
        error.append("Please enter a start date.")
    if len(plan['endDate'])==0:
        isValid=False
        error.append("Please enter an end date.")
    if string>startDate:
        isValid = False
        error.append("Start Date must be in the future.")
    if startDate>endDate:
        isValeid = False
        error.append("End Date must be after the start date.")
    return {"isValid":isValid, "errors":error}
