import dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly_express as px
from dash import dcc, html, callback, Output, Input

from dataframe import data_frame

dash.register_page(__name__, path='/', name='Home')

df = data_frame()

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Row(html.H2("Bar Graph")),
            dbc.Row(html.Hr()),
            dbc.Row(dcc.Graph(id='vehicle-graph-line'))
        ]),
        dbc.Col([
            dbc.Row(html.H2("Line Graph")),
            dbc.Row(html.Hr()),
            dbc.Row(dcc.Graph(id='vehicle-graph'))
        ])
    ])
])


@callback(
    Output('vehicle-graph', 'figure'),
    Output('vehicle-graph-line', 'figure'),
    Input('radioitems-input', 'value')
)
def update_graph(selected_quarter):
    traces = []
    colors = ['rgba(0, 0, 255, 0.5)', 'rgba(255, 0, 0, 0.5)', 'rgba(0, 255, 0, 0.5)', 'rgba(0, 255, 255, 0.5)']
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']

    if selected_quarter == 5:
        for quarter in range(1, selected_quarter):
            quarter_data = df[df['Quarter'] == quarter]
            trace = go.Bar(
                x=quarter_data['Year'],
                y=quarter_data['New Vehicles'],
                name=quarters[quarter - 1],
                marker_color=colors[quarter - 1],
                showlegend=(quarter == 1 or quarter == 2 or quarter == 3 or quarter == 4)
            )
            traces.append(trace)
    else:
        quarter_data = df[df['Quarter'] == selected_quarter]
        trace = go.Bar(
            x=quarter_data['Year'],
            y=quarter_data['New Vehicles'],
            name=quarters[selected_quarter - 1],
            marker_color=colors[selected_quarter - 1],
            showlegend=(
                    selected_quarter == 1 or selected_quarter == 2 or selected_quarter == 3 or selected_quarter == 4)
        )
        traces.append(trace)

    fig = go.Figure(data=traces)
    fig.update_layout(
        title='Tesla New Vehicle Production Bar Graph',
        xaxis_title='Year',
        yaxis_title='New Vehicles',
        legend_title_text='Quarter',
        barmode='group'
    )

    if selected_quarter == 5:
        line = px.line(df, x="Year", y="New Vehicles", color="Quarter")
    else:
        line = px.line(df[df['Quarter'] == selected_quarter], x="Year", y="New Vehicles", color="Quarter")
    line.update_layout(
        title="Tesla New Vehicle Production Line Graph",
        xaxis_title='Year',
        yaxis_title='New Vehicles',
        legend_title_text='Quarter'
    )
    return fig, line
