import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd

dash.register_page(__name__, name="Icicle", title="Icicle")

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(
    go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        root_color="lightblue",
        tiling = dict(
            orientation='v'
        )
    )
)
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

layout=html.Div([html.H2('Icicle Graph'),
                dcc.Graph(figure=fig)])