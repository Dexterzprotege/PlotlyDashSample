import base64

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

df = pd.read_csv("assets/tesla_vehicles.csv")

image_path = "assets/tesla-logo.png"
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

SIDEBAR_STYLE = {
    "position": "relative",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa"
}


def nav_bar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.Row(
                    [
                        dcc.Link(html.Img(src="data:image/png;base64," + encoded_image, height="30px"), href="/",
                                 className="nav-link")
                    ],
                    align="center",
                    className="g-0"
                ),
                dbc.Nav(
                    [
                        dbc.NavItem(dcc.Link("Page 1", href="/", className="nav-link")),
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
    sidebar = html.Div(
        [
            html.H4("Sidebar", className="display-9", style={'textAlign': 'center'}),
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
        ], style=SIDEBAR_STYLE)
    return sidebar
