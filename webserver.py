# pip install snowflake-connector-python
# pip install snowflake-sqlalchemy


from flask import Flask
from snowflake import connector

app = Flask("My Website")

@app.route("/")
def home():
    return "Weclome to my website!  My snowflake account # is: " + str(onerow)

@app.route("/about")
def about():
    return "About my website!"

# Credentials
file = open("credentials", "r")
credentials = json.load(file)
file.close()


# Snowflake
cnx = connector.connect(
    account = "ci21584.ca-central-1.aws",
    user = "datacrunch",
    password = "Enterprise1!"
)

cur = cnx.cursor()
cur.execute("select current_account()")
onerow = cur.fetchone()

app.run()
