import pyodbc 
import pandas as pd
import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="Graph & RangeSlider", title="Graph & RangeSlider")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HIMARY\SQLEXPRESS;'
                      'Database=SbonDB;'
                      'Trusted_Connection=yes;')

query='SELECT SUM(SUMA) as SUMA, CAST(DATADOC as DATE) as DATE FROM dbo.PLAT GROUP BY CAST(DATADOC as DATE) order by CAST(DATADOC as DATE) desc'
df= pd.read_sql_query(query, conn, parse_dates='DATE')

layout=html.Div([
    dbc.Row(
        dbc.Col(dcc.RangeSlider(
            id='DateRange',
            min=0,
            max=len(df) - 1,
            marks={i: str(df['DATE'][i].date()) for i in range(0, len(df), int(len(df) / 5))},
            value=[0, len(df) - 1],
            step=1,  # Set the step size to 1 to move one data point at a time
            #tooltip={'always visible': True, 'placement': 'bottom'}
        ), width=10, style = {'margin-left':'95px', 'margin-bottom':'20px'})),
    dbc.Row(
        dbc.Col(
            html.Div(dcc.Graph(id='MyChart')
        )))     
     
])

@callback(
    Output('MyChart', 'figure'),
    [Input('DateRange', 'value')]
)
def update_graph(selected_indices):
    selected_data = df.iloc[selected_indices[0]:selected_indices[1] + 1]
    
    fig = px.line(selected_data, x='DATE', y='SUMA', labels={'x': 'DATE', 'y': 'SUMA'})
    return fig


