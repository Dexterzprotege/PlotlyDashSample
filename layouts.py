import base64

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

df = pd.read_csv("assets/tesla_vehicles.csv")

image_path = "assets/tesla-logo-png-2244.png"
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

SIDEBAR_STYLE = {
    "position": "relative",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "3rem 2rem",
    "background-color": "#f8f9fa"
}


def nav_bar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.Div(
                    [
                        dcc.Link(
                            html.Img(src="data:image/png;base64," + encoded_image, height="20px"),
                            href="/",
                            className="nav-link",
                            style={"float": "left"}
                        ),
                    ],
                    className="mr-auto"
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
        color="#F80115",
        dark=True
    )

    return navbar


def side_bar():
    sidebar = html.Div(
        [
            html.H3("Sidebar", className="display-8", style={'textAlign': 'center'}),
            html.Hr(),
            html.Div([
                dbc.Label("Select a Quarter: "),
                dbc.RadioItems(
                    options=[
                        {"label": "Quarter 1", "value": 1},
                        {"label": "Quarter 2", "value": 2},
                        {"label": "Quarter 3", "value": 3},
                        {"label": "Quarter 4", "value": 4},
                        {"label": "All Quarters", "value": 5},
                    ],
                    value=5,
                    id="radioitems-input",
                ),
            ])
        ], style=SIDEBAR_STYLE)
    return sidebar
