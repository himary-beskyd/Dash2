import dash
from dash import html

dash.register_page(__name__, path='/', title="Home", image="Image2.png", description="This is Home page")

layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
    html.Div(html.Img(src=dash.get_asset_url('Image2.png'), style={'height':'80%','width':'80%'}), style={'textAlign':'center'})
    ])
