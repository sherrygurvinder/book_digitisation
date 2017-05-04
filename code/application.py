from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session

# configure application
app = Flask(__name__)

@app.route("/")

def index():
    print("helllo.................................")
    return render_template("login.html")
    #return apology("index")