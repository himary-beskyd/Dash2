import pyodbc 
import pandas as pd
import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

dash.register_page(__name__, name="Graph & Table", title="Graph & More")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HIMARY\SQLEXPRESS;'
                      'Database=SbonDB;'
                      'Trusted_Connection=yes;')

df_table = pd.read_sql_query('SELECT ACTION_CODE, PROC_CODE_ID, NAME FROM dbo.RB_CLASSIFIER', conn)

df_graph1= pd.read_sql_query('SELECT SUM(SUMA) as SUMA, CAST(DATADOC as DATE) as DATE FROM dbo.PLAT GROUP BY CAST(DATADOC as DATE) order by CAST(DATADOC as DATE) desc', conn)

layout = html.Div(
    [
        dbc.Row(
            [
                #dbc.Col(html.Div(dcc.Graph(id="graph1", figure=f1))),
                dbc.Col(dash_table.DataTable(data=df_table.to_dict('records'),
                                  columns=[{"name": i, "id": i} for i in df_table.columns],
                                  #fill_width=True,
                                  filter_action="native",
                                  fixed_rows={ 'headers': True, 'data': 0 },
                                  style_cell={'textAlign': 'left'},
                                  #style_as_list_view=True,
                                  style_header={'fontWeight': 'bold',
                                                 'backgroundColor': 'rgb(3, 128, 252)',
                                                 'color': 'white'}, 
                                  style_data={'color': 'black',
                                              'backgroundColor': 'rgb(235, 239, 242)' 
                                             }                                                                                                                                                     
                                  ), width=6),
                dbc.Col(html.Div(dcc.Graph(id="graph1", figure=go.Figure(data=[go.Scatter(x=df_graph1["DATE"], y=df_graph1["SUMA"])],
                                                                         layout=go.Layout(
                                                                             xaxis={
                                                                                 'rangeslider': {'visible':True},
                                                                                 'rangeselector': {'visible':True, 'buttons': [{'step':'all'}, {'step':'day'}]}
                                                                             },
                                                                         ) ))), width=6),                
            ]
        ),
    ]
)

