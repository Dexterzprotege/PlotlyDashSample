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
    Input('radioitems-input', 'value'),
    Input('input1', 'value'),
    Input('input2', 'value')
)
def update_graph(selected_quarter, start_year, end_year):
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
    traces = []
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    totals = []

    if selected_quarter == 5:
        for quarter in range(1, selected_quarter):
            quarter_data = filtered_df[filtered_df['Quarter'] == quarter]
            trace = go.Bar(
                x=quarter_data['Year'],
                y=quarter_data['New Vehicles'],
                name=quarters[quarter - 1],
                showlegend=(quarter == 1 or quarter == 2 or quarter == 3 or quarter == 4)
            )
            totals.append(quarter_data['New Vehicles'])
            traces.append(trace)
    else:
        quarter_data = filtered_df[filtered_df['Quarter'] == selected_quarter]
        trace = go.Bar(
            x=quarter_data['Year'],
            y=quarter_data['New Vehicles'],
            name=quarters[selected_quarter - 1],
            showlegend=(
                    selected_quarter == 1 or selected_quarter == 2 or selected_quarter == 3 or selected_quarter == 4)
        )
        totals.append(quarter_data['New Vehicles'])
        traces.append(trace)

    fig = go.Figure(data=traces)
    fig.update_layout(
        title='Tesla New Vehicle Production Bar Graph',
        width=600,
        height=500,
        template="simple_white",
        xaxis_title='Year',
        yaxis_title='New Vehicles',
        legend_title_text='Quarter',
        barmode='group'
    )

    if selected_quarter == 5:
        line = px.line(filtered_df, x="Year", y="New Vehicles", color="Quarter")
    else:
        line = px.line(filtered_df[filtered_df['Quarter'] == selected_quarter], x="Year", y="New Vehicles",
                       color="Quarter")
    line.update_layout(
        title="Tesla New Vehicle Production Line Graph",
        width=600,
        height=500,
        template="simple_white",
        xaxis_title='Year',
        yaxis_title='New Vehicles',
        legend_title_text='Quarter',
    )
    return line, fig
