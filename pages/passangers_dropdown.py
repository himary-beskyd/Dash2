import pandas as pd
import dash
from dash import html, dcc, callback, Output, Input
import plotly.express as px

dash.register_page(__name__, name="Passangers & Dropdown", title="Passangers & Dropdown")

df=pd.read_excel(r"C:\Users\himar\Desktop\Work\Data for Dash\data_1.xlsx", sheet_name='Sheet2')

# Define the layout of the app
layout = html.Div([
    html.Label('Select Country:'),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['Country'].unique()],
        value=df['Country'].iloc[0]
    ),
    
    html.Label('Select Year Range:'),
    dcc.RangeSlider(
        id='year-slider',
        min=df['Time'].min(),
        max=df['Time'].max(),
        marks={str(year): str(year) for year in df['Time'].unique()},
        step=1,
        value=[df['Time'].min(), df['Time'].max()]
    ),
    
    dcc.Graph(id='graph')
])

# Define callback to update the graph based on dropdown and slider values
@callback(
    Output('graph', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('year-slider', 'value')]
)
def update_graph(selected_country, selected_year_range):
    # Filter data based on selected values
    filtered_df = df[(df['Country'] == selected_country) &
                     (df['Time'] >= selected_year_range[0]) &
                     (df['Time'] <= selected_year_range[1])]
    
    # Create a new chart using Plotly Express
    fig = px.bar(
        filtered_df,
        x='Time',  # Replace with your actual column name
        y='Number of passangers',  # Replace with your actual column name
        labels={'y': f'{selected_country} - {selected_year_range[0]} to {selected_year_range[1]}'},
        title=f'{selected_country} - {selected_year_range[0]} to {selected_year_range[1]}'
    )
    
    return fig