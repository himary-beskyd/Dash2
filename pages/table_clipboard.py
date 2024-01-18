import dash
from dash import Dash, dcc, html, Input, Output, State, dash_table, callback
import pandas as pd
import pyodbc

dash.register_page(__name__, name="Table & Clipboard", title="Table & Clipboard")

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HIMARY\SQLEXPRESS;'
                      'Database=SbonDB;'
                      'Trusted_Connection=yes;')

df = pd.read_sql_query('SELECT ACTION_CODE, PROC_CODE_ID, NAME FROM dbo.RB_CLASSIFIER', conn)

layout = html.Div(
    [
        dcc.Clipboard(id="table_copy", style={"fontSize":20}),
        dash_table.DataTable(df.to_dict('records'),
                                  [{"name": i, "id": i} for i in df.columns],
                                  filter_action="native",
                                  fixed_rows={ 'headers': True, 'data': 0 },
                                  style_cell={'textAlign': 'left'},                            
                                  id="table_cb",
                                  #style_as_list_view=True,
                                  style_header={'fontWeight': 'bold',
                                                 'backgroundColor': 'rgb(3, 128, 252)',
                                                 'color': 'white'}, 
                                  style_data={'color': 'black',
                                              'backgroundColor': 'rgb(235, 239, 242)' 
                                             }                                                                                               
                            )
    ]
)


@callback(
    Output("table_copy", "content"),
    Input("table_copy", "n_clicks"),
    State("table_cb", "data"),
)
def custom_copy(_, data):
    dff = pd.DataFrame(data)
    # See options for .to_csv() or .to_excel() or .to_string() in the  pandas documentation
    return dff.to_csv(index=False)  # includes headers

