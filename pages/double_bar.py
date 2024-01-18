import plotly.express as px
import dash
from dash import dcc

dash.register_page(__name__, name="Double Bar", title="Double Bar")


df = px.data.tips()
fig = px.histogram(df, x="day", y="total_bill", color="sex")

fig.add_shape( # add a horizontal "target" line
    type="line", line_color="salmon", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=1, xref="paper", y0=700, y1=700, yref="y"
)

fig.add_annotation( # add a text callout with arrow
    text="below target!", x="Fri", y=400, arrowhead=1, showarrow=True
)

layout=dcc.Graph(figure=fig)