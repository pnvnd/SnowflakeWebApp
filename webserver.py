# pip install snowflake-connector-python
# pip install snowflake-sqlalchemy

import json
from flask import Flask, render_template, request
from snowflake import connector
import pandas as pd

app = Flask("My Website")

@app.route("/")
def home():
    return render_template("index.html", dfhtml=dfhtml)

@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/thanks4submit", methods=["POST"])
def thanks():
    colorname = request.form.get("cname")
    username = request.form.get("uname")
    return render_template("thanks4submit.html", colorname=colorname, username=username)

# Credentials
file = open("credentials", "r")
credentials = json.load(file)
file.close()


# Snowflake
cnx = connector.connect(
    account = credentials["account"],
    user = credentials["user"],
    password = credentials["password"],
    warehouse = credentials["warehouse"],
    database = credentials["database"],
    schema = credentials["schema"],
    role = "SYSADMIN"
)

cur = cnx.cursor()
cur.execute("select * from colors")
rows = pd.DataFrame(cur.fetchall(), columns=["Color UID", "Color Name"])
#print(rows)
#onerow = cur.fetchone()

# test dataframe as html
dfhtml = rows.to_html()
#print(dfhtml)

app.run()
