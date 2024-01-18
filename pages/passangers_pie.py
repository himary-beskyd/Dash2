import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

dash.register_page(__name__, name="Passangers & Pie", title="Passangers & Pie")

df=pd.read_excel(r"C:\Users\himar\Desktop\Work\Data for Dash\data_1.xlsx", sheet_name='Sheet3')

# Layout of the app
layout = html.Div(children=[
    html.H1(children='Passangers'),

    dcc.Graph(
        id='pie-chart',
        figure=px.pie(df, values='Passangers', names='Country', width=1200, height=550),
        )
])