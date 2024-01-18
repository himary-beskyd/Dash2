import dash
from dash import Dash, dcc, html
import plotly.express as px
from base64 import b64encode
import io

dash.register_page(__name__, name="Graph & Html", title="Graph & Html")

buffer = io.StringIO()

df = px.data.iris() # replace with your own data source
fig = px.scatter(
    df, x="sepal_width", y="sepal_length", 
    color="species")
fig.write_html(buffer)

html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

layout = html.Div([
    html.H4('Simple plot export options'),
    html.P("↓↓↓ try downloading the plot as PNG ↓↓↓", style={"text-align": "right", "font-weight": "bold"}),
    dcc.Graph(id="graph", figure=fig),
    html.A(
        html.Button("Download as HTML",
                    style={'backgroundColor': 'rgb(3, 128, 252)',
                           'color':'white','width':'15%','height': '50px','text-align':'center', 'marginLeft': '20px', 'marginBottom': 10}), 
        id="download",
        href="data:text/html;base64," + encoded,
        download="plotly_graph.html"
    )
])
