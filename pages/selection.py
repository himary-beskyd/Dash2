import dash
from dash import dcc
import plotly.express as px

dash.register_page(__name__, name="Selection", title="Selection")

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.add_selection(x0=3.0, y0=6.5, x1=3.5, y1=5.5)

fig.update_layout(dragmode='select',
                  activeselection=dict(fillcolor='yellow'))

layout=dcc.Graph(figure=fig)