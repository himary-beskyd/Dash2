import dash
from dash import dcc
import plotly.graph_objects as go

dash.register_page(__name__, name="Map", title="Map")

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=110, scope="europe",
    showcountries=True, countrycolor="Black",
    #showsubunits=True, subunitcolor="Blue",
    lataxis_range=[44,53], lonaxis_range=[22, 41]
)
fig.update_layout(height=600,
                  margin={"r":0,"t":0,"l":0,"b":0})


layout=dcc.Graph(figure=fig)