from dash import Dash, dcc, Output, Input, html
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px
import base64
import pandas as pd

df = pd.read_csv("tesla_vehicles.csv")

image_path = "tesla-logo.png"
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

SIDEBAR_STYLE = {
    "position": "absolute",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa"
    # "z-index": 99999
}

CONTENT_STYLE = {
    "top": 0,
    "margin-top": '2rem',
    "margin-left": "18rem",
    "margin-right": "2rem",
}

def nav_bar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dcc.Link(html.Img(src="data:image/png;base64," + encoded_image, height="30px"), href="/", className="nav-link")
                    ],
                    align="center",
                    className="g-0"
                ),
                dbc.Nav(
                    [
                        dbc.NavItem(dcc.Link("Page 1", href="/page1", className="nav-link")),
                        dbc.NavItem(dcc.Link("Page 2", href="/page2", className="nav-link")),
                    ],
                    className="ml-auto",
                    navbar=True
                ),
            ],
        ),
        color="dark",
        dark=True,
    )

    return navbar

def side_bar():
    sidebar =  html.Div(
    [
        html.H4("Sidebar", className="display-9",style={'textAlign':'center'}),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                dcc.RangeSlider(
                    id='year-range-slider',
                    min=df['Year'].min(),
                    max=df['Year'].max(),
                    marks={str(year): str(year) for year in df['Year'].unique()},
                    value=[df['Year'].min(), df['Year'].max()],
                    step=None,
                ), style={'transform': 'rotate(270deg)', 'marginTop': '100px', 'width': '100%', 'height': '100%'}
            )]),
    ],style=SIDEBAR_STYLE)
    return sidebar

layout1 = html.Div([
    html.H2("Page 1 (Graph)"),
    html.Hr(),
    dbc.Container([
        dbc.Row(dcc.Graph(id='vehicle-graph'), justify='center'),
    ], fluid=True)
])

layout2 = html.Div(
    [
        html.H2('Page 2 (Table)'),
        html.Hr(),
        dbc.Container(
            dbc.Row([dbc.Col(dcc.Graph(id='vehicle-table'), width=6)], justify='center'),
        )
    ])