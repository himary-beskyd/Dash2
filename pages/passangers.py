import pandas as pd
import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px

dash.register_page(__name__, name="Passangers", title="Passangers")

df=pd.read_excel(r"C:\Users\himar\Desktop\Work\Data for Dash\data_1.xlsx", sheet_name='Sheet1')

layout= html.Div([
    html.H1('Passangers in Bulgaria', style={'textAlign': 'left'}),
    dcc.Graph(figure=px.bar(df, x='TIME', y='Bulgaria', template='minty'))
]) 

