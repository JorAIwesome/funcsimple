import os
import pyodbc
from get_secret import get_secret

# Retrieve environment mode
env_mode = os.getenv('ENV_MODE')

if env_mode != 'production':
    conn_string = 'DRIVER={SQL Server};SERVER=localhost,1433;DATABASE='+os.getenv('EMULATOR_DATABASE_NAME')+';UID='+os.getenv('EMULATOR_DATABASE_UID')+';PWD='+os.getenv('EMULATOR_DATABASE_PWD')
else:
    sql_database = "..."
    database = get_secret("SQL_DATABASE")
    username = get_secret("SQL_USERNAME")
    password = get_secret("SQL_PASSWORD")
    conn_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:"+sql_database+".database.windows.net,1433;DATABASE="+database+";UID="+username+";PWD="+password+";"

conn = pyodbc.connect(conn_string)
cursor = conn.cursor()