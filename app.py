import os
from flask import Flask, flash, render_template, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import requests
import sqlite3

from helpers import login_required, get_recipe

app = Flask(__name__)
#configure session
app.secret_key = "key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

#connect to database
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('recipes.db', check_same_thread=False)
    except sqlite3.error as e:
        print(e)
    return conn

#landing page
@app.route('/', methods=["GET", "POST"])
def homepage():
    db = db_connection()
    cursor = db.cursor()
    if request.method == "GET":
        return render_template("home.html")

    if request.method == "POST":
        return render_template("home.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    #connect to database
    db = db_connection()
    cursor = db.cursor()
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        #ensure info entered properly
        if not request.form.get("newUser"):
            return render_template("error.html")
        if not request.form.get("newPassword"):
            return render_template("error.html")
        if not request.form.get("Confirmation"):
            return render_template("error.html")

        password = request.form.get("newPassword")
        confirmation = request.form.get("Confirmation")

        if password != confirmation:
            return render_template("error.html")

        newUser = request.form.get("newUser")
        passwordhash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        try:
            cursor.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (newUser, passwordhash))
            db.commit()
        except:
            return render_template("errorlog.html")

        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    #connect to database
    db = db_connection()
    cursor = db.cursor()

   #forget user_id
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        if not request.form.get("user"):
            return render_template("error.html")

        elif not request.form.get("password"):
            return render_template("error.html")

        user = request.form.get("user")
        cursor.execute("SELECT * FROM users WHERE username = ?", (user,))
        users = cursor.fetchall()
        #hashQuery = cursor.execute("SELECT hash FROM users WHERE username = ?", (user,))
        #pHash = cursor.fetchall()
        passIn = request.form.get("password")
        #idQuery = cursor.execute("SELECT id FROM users WHERE username = ?", (user, ))
        #id = cursor.fetchall()

        #check there is only one user with such name and password is correct
        if check_password_hash(users[0]["hash"], passIn) == False:
            return render_template("errorlog.html")

        cursor.close()

        #remember active user
        session["user_id"] = id[0]

        return redirect("/")

@app.route("/pantry", methods=["GET", "POST"])
def pantry():
    if request.method == "GET":
        return render_template("pantry.html")
    if request.method == "POST":
        ingredients = request.form.get("ingredient").strip()
        try:
            url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

            querystring = {"ingredients": ingredients, "number": "5", "ignorePantry": "false", "ranking": "1"}

            headers = {
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "3a0459353amsh5d58f0cb91c5ebep144016jsn2e9b23ae44f3"
            }

            response = requests.request("GET", url, headers=headers, params=querystring).json()

            return render_template("results.html", recipes=response, get_recipe=get_recipe)
        except requests.RequestException:
            return None



if __name__ == '__main__':
    app.run(debug=False)
