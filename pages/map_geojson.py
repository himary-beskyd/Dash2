import pandas as pd
import urllib.request
import json
import plotly.graph_objects as go
import dash
from dash import html, dcc
import numpy as np


#url="C:\Users\himar\Desktop\Work\Data for Dash\ukraine-with-regions_1530.geojson"

dash.register_page(__name__, name="Map & Geojson", title="Map & Geojson")

def read_geojson(url):
    with open(url) as f:
        jdata = json.loads(f.read())
    return jdata 

jdata = read_geojson(r"C:\Users\himar\Desktop\Work\Data for Dash\ukraine-with-regions_1530.geojson")

df=pd.read_csv(r"C:\Users\himar\Desktop\Work\Data for Dash\Ukraine_regions_data.csv")

mycustomdata = np.stack((df['oblast-name'], df['2022']), axis=-1)

title = 'Ukrainian Choroplethmapbox'

fig = go.Figure(go.Choroplethmapbox(geojson=jdata, 
                                    locations=df['oblast-name'], 
                                    z=df['2022'],
                                    featureidkey='properties.name',
                                    #coloraxis="coloraxis4",
                                    colorscale='Blues',
                                    customdata=mycustomdata,
                                    hovertemplate= 'Oblast: %{customdata[0]}'+\
                                                   '<br>2022: %{customdata[1]}<extra></extra>',
                                    #marker_line_width=1
                                    ))


fig.update_layout(title_text = title,
                  title_x=0.5,
                  mapbox=dict(style='carto-positron',
                              zoom=4.88, 
                              center = {"lat": 48.525888 , "lon":31.105833 },
                              ),
                  width=1200,
                  height=550,
                  margin=dict(l=20, r=20, t=40, b=0),
                  #geo_resolution=50
                  ); 

layout=html.Div([#html.H1('Map from GeoJSON'),
                 dcc.Graph(figure=fig)])
