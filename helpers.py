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
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

        querystring = {"ingredients": "apples,flour,sugar", "number": "5", "ignorePantry": "true", "ranking": "2"}

        headers = {
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "3a0459353amsh5d58f0cb91c5ebep144016jsn2e9b23ae44f3"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
    except requests.RequestException:
        return None

def get_recipe(id):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/479101/information"

    headers = {
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "3a0459353amsh5d58f0cb91c5ebep144016jsn2e9b23ae44f3"
    }

    response = requests.request("GET", url, headers=headers).json()

    link = response['sourceUrl']

    return link

