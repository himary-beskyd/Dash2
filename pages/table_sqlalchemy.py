import dash
from dash import html, callback, dash_table
from dash.dependencies import Input, Output
import sqlalchemy as db
from sqlalchemy import text
import pandas as pd

# Replace these values with your actual database credentials
username = "Mariia"
password = "sbon+"
server = r"DESKTOP-HIMARY\SQLEXPRESS"
database = "SbonDB"

dash.register_page(__name__, name='Table & SQLAlchemy', title='Table & SQLAlchemy')

# Connection string with ODBC Driver 17 for SQL Server
mssql_connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

# Create the SQLAlchemy engine
engine = db.create_engine(mssql_connection_string)

query="SELECT ACTION_CODE, PROC_CODE_ID, NAME FROM dbo.RB_CLASSIFIER"
    # Execute SQL query to fetch data
with engine.connect() as connection:
    result = connection.execute(text(query))
    df = pd.DataFrame(result, columns=result.keys())

# Define the layout
layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns = [{'name': col, 'id': col} for col in df.columns],  # Columns will be dynamically updated based on the query result
        data = df.to_dict('records')
    )
])


