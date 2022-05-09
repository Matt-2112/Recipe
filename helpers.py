from flask import request, redirect, session
import requests
from functools import wraps
import os

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def lookup(list):
    try:
        api_key=os.environ.get("API_KEY")
        url = f""
    except requests.RequestException:
        return None