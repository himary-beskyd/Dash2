import pyodbc 
import pandas as pd
import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
from collections import OrderedDict

dash.register_page(__name__, name='Table')

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HIMARY\SQLEXPRESS;'
                       'Database=SbonDB;'
                      'Trusted_Connection=yes;')

df = pd.read_sql_query('SELECT ACTION_CODE, PROC_CODE_ID, NAME FROM dbo.RB_CLASSIFIER', conn)

layout = html.Div([
    html.Button("Download Excel",
                id="btn_xlsx",
                style={'backgroundColor': 'rgb(3, 128, 252)', 'color':'white','width':'10%','height': '50px','text-align':'center', 'marginLeft': '20px', 'marginTop': 20, 'marginBottom': 10}),
    dcc.Download(id="download-dataframe-xlsx"),
    dash_table.DataTable(
        style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'color': 'black',
        'backgroundColor': 'rgb(223, 227, 230)'
        },
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        filter_action="native",
        fixed_rows={ 'headers': True, 'data': 0 },
        style_cell={'textAlign': 'left',
                    #'height': 'auto',
                    # all three widths are needed
                    'minWidth': '20px', 'width': '60px', 'maxWidth': '180px',
                    'whiteSpace': 'normal',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis'},
        #style_as_list_view=True,
        style_header={'fontWeight': 'bold',
                      'backgroundColor': 'rgb(3, 128, 252)',
                      'color': 'white'}, 
        page_size=10,
        tooltip_data=[{
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
            }
            for row in df.to_dict('records')
        ],
        tooltip_duration=None                                                                                           
        )
])

@callback(
    Output("download-dataframe-xlsx", "data"),
    Input("btn_xlsx", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_excel, "mydf.xlsx", sheet_name="Sheet_name_1")

