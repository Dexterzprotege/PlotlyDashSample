from dash import Dash, dcc, Output, Input, html
from app import app
from layouts import nav_bar, side_bar, layout1, layout2, CONTENT_STYLE
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav_bar(),
    side_bar(),
    html.Div(id='page-content',style=CONTENT_STYLE)
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return layout1
    elif pathname == '/page1':
        return layout1
    elif pathname == '/page2':
         return layout2
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)