# pip install snowflake-connector-python
# pip install snowflake-sqlalchemy

import json
from snowflake import connector

def sfconnect():
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
        role = "SYSADMIN")
    return cnx