import dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dcc, html, callback, Output, Input

from dataframe import data_frame

dash.register_page(__name__, path="/page2", name='Page 2')

df = data_frame()

layout = html.Div([
    html.H2('Page 2 (Table)'),
    html.Hr(),
    dbc.Container(
        dbc.Row([dbc.Col(dcc.Graph(id='vehicle-table'), width=6)], justify='center'),
    )
])


@callback(
    Output('vehicle-table', 'figure'),
    Input('year-range-slider', 'value')
)
def update_table(selected_years):
    start_year, end_year = selected_years
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
    table_trace = go.Table(
        header=dict(values=filtered_df.columns,
                    line_color='darkslategray',
                    fill_color='lightskyblue',
                    align='left'),
        cells=dict(values=[filtered_df.Year, filtered_df.Quarter, filtered_df['New Vehicles']],
                   line_color='darkslategray',
                   fill_color='lightcyan',
                   align='left')
    )
    table = go.Figure(data=[table_trace])
    return table
