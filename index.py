import dash
import dash_bootstrap_components as dbc
from dash import html
from dash_bootstrap_templates import load_figure_template

from layouts import nav_bar, side_bar

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.LUX])
load_figure_template('LUX')

app.layout = html.Div([
    nav_bar(),
    html.Br(),
    dbc.Row(
        [
            dbc.Col(
                [
                    side_bar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ],
    )
])


if __name__ == '__main__':
    app.run(debug=True)