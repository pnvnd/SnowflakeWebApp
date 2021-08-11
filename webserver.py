# Import packages
from flask import Flask, render_template, request
import pandas as pd
from snowflakeConnection import sfconnect

# Flask Web Application
app = Flask("Snowflake WebApp")

@app.route("/")
def home():
    cur = cnx.cursor().execute("select color_name, count(*) "
                                "from colors "
                                "group by color_name "
                                "having count(*) > 50 "
                                "order by count(*) desc;")
    rows = pd.DataFrame(cur.fetchall(), columns=["Color Name", "Votes"])
    dfhtml = rows.to_html(index=False)
    return render_template("index.html", dfhtml=dfhtml)

@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/thanks4submit", methods=["POST"])
def thanks():
    colorname = request.form.get("cname")
    username = request.form.get("uname")
    cnx.cursor().execute("insert into colors (color_uid, color_name) " +
                         "select color_uid_seq.nextval, '" + colorname + "'")
    return render_template("thanks4submit.html", colorname=colorname, username=username)

@app.route("/charts")
def charts():
    cur = cnx.cursor().execute("select color_name, count(*) "
                                "from colors "
                                "group by color_name "
                                "order by count(*) desc;")
    data4charts = pd.DataFrame(cur.fetchall(), columns=["color", "votes"])
    #data4charts.to_csv("data4charts.csv", index=False)
    data4ChartsJSON = data4charts.to_json(orient="records")
    return render_template("charts.html", data4ChartsJSON=data4ChartsJSON)

# Snowflake
cnx = sfconnect()

#print(rows)
#onerow = cur.fetchone()
# test dataframe as html
#print(dfhtml)

app.run()
