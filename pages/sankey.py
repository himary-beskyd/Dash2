import dash
from dash import dcc, html, Input, Output, callback
import plotly.graph_objects as go
import json, urllib

dash.register_page(__name__, suppress_callback_exceptions=True, name="Sankey", title="Sankey")

layout = html.Div([
    html.H4('Supply chain of the energy production'),
    dcc.Graph(id="graph"),
    html.P("Opacity"),
    dcc.Slider(id='slider', min=0, max=1, 
               value=0.5, step=0.1)
])

@callback(
    Output("graph", "figure", allow_duplicate=True), 
    Input("slider", "value"),
    prevent_initial_call='intial duplicate')
def display_sankey(opacity):
    url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read()) # replace with your own data source

    node = data['data'][0]['node']
    node['color'] = [
        f'rgba(255,0,255,{opacity})' 
        if c == "magenta" else c.replace('0.8', str(opacity)) 
        for c in node['color']]

    link = data['data'][0]['link']
    link['color'] = [
        node['color'][src] for src in link['source']]

    fig = go.Figure(go.Sankey(link=link, node=node))
    fig.update_layout(font_size=10)
    return fig