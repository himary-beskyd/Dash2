import dash
from dash import Dash, dcc, html, Input, Output, callback
from plotly.subplots import make_subplots
import plotly.graph_objects as go

dash.register_page(__name__, name="Subplots", title="Subplots")

layout = html.Div([
    html.H4('Live adjustable subplot-width'),
    dcc.Graph(id="graph"),
    html.P("Subplots Width:"),
    dcc.Slider(
        id='slider-width', min=.1, max=.9, 
        value=0.5, step=0.1)
])


@callback(
    Output("graph", "figure", allow_duplicate=True), 
    Input("slider-width", "value"),
    prevent_initial_call="initial duplicate")

def customize_width(left_width):
    fig = make_subplots(rows=1, cols=2, 
        column_widths=[left_width, 1 - left_width])

    fig.add_trace(row=1, col=1,
        trace=go.Scatter(x=[1, 2, 3], y=[4, 5, 6])) # replace with your own data source

    fig.add_trace(row=1, col=2,
        trace=go.Scatter(x=[20, 30, 40], y=[50, 60, 70]))
    return fig
