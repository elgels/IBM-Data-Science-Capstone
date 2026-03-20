import os
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "data", "spacex_launch_dash.csv")

spacex_df = pd.read_csv(file_path)

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard",
            style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
        ],
        value='ALL'
    ),

    dcc.Graph(id='success-pie-chart'),

    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=1000,
        value=[min_payload, max_payload]
    ),

    dcc.Graph(id='success-payload-scatter-chart')
])

# Callbacks
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie(site):
    if site == 'ALL':
        df = spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        fig = px.pie(df, values='class', names='Launch Site')
    else:
        df = spacex_df[spacex_df['Launch Site'] == site]
        df = df.groupby('class').size().reset_index(name='count')
        fig = px.pie(df, values='count', names='class')
    return fig


@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter(site, payload):
    low, high = payload
    df = spacex_df[spacex_df['Payload Mass (kg)'].between(low, high)]

    if site != 'ALL':
        df = df[df['Launch Site'] == site]

    fig = px.scatter(
        df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category'
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)
