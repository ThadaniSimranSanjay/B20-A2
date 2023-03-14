from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

# connect to the SQL Database
con = sqlite3.connect("database.db")
cur = con.cursor()


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/")
def user():
    return render_template("user.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")

app.run(host='0.0.0.0', port=81, debug=True)
