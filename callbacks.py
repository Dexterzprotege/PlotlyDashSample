from dash import Dash, dcc, Output, Input, html
from layouts import df
from app import app
import plotly.graph_objects as go

@app.callback(
    Output('vehicle-graph', 'figure'),
    Input('year-range-slider', 'value')
)
def update_graph(selected_years):
    start_year, end_year = selected_years
    filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
    traces = []
    colors = ['rgba(0, 0, 255, 0.5)', 'rgba(255, 0, 0, 0.5)', 'rgba(0, 255, 0, 0.5)', 'rgba(0, 255, 255, 0.5)']
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']

    for quarter in range(1, 5):
        quarter_data = filtered_df[filtered_df['Quarter'] == quarter]
        trace = go.Bar(
            x=quarter_data['Year'],
            y=quarter_data['New Vehicles'],
            name=quarters[quarter-1],
            marker_color=colors[quarter-1],
            showlegend=(quarter == 1 or quarter == 2 or quarter == 3 or quarter == 4)  # Set showlegend to True only for the first trace of each quarter
        )
        traces.append(trace)

    fig = go.Figure(data=traces)
    fig.update_layout(
        title='Tesla New Vehicle Production by Year and Quarter',
        xaxis_title='Year',
        yaxis_title='New Vehicles',
        legend_title_text='Quarter',
        barmode='group'
    )
    return fig

@app.callback(
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