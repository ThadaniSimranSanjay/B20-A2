from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dkf3sldkjfDF23fLJ3b'


# connect to the SQL Database
con = sqlite3.connect("database.db")
cur = con.cursor()

# Creating the User table
sql_query = """
    CREATE TABLE IF NOT EXISTS User 
    (
        username TEXT PRIMARY KEY, 
        password TEXT, 
        role TEXT
    )
"""

cur.execute(sql_query)
print("hello" + sql_query)


@app.route("/")
def user():
    return render_template("user.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/api/register", methods=['GET', 'POST'])
def register():
    if(request.method == "POST"):
        print("testing")

        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        try:
            sql_query = "INSERT INTO User VALUES ('"
            sql_query += username + "', '" + password + "', '" + role + "')"
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute(sql_query)
            con.commit()  # commit the results
            print("sql query:" + sql_query)
            flash("User successfully created")
            return render_template("signup.html")
            # return redirect(url_for('register'))
        except sqlite3.IntegrityError:
            flash("User already exists, please enter a different username")
            return render_template("signup.html")
    else:
        return render_template('signup.html')


@app.route("/api/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


# app.run(host='0.0.0.0', port=81, debug=True)
