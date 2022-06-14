# Run this app with `python simple_app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Run this app with `python simple_app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

app = Dash(external_stylesheets=[dbc.themes.LUX])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("all_apps/appdata/car data.csv")

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "0rem",
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "background-color": "#f8f9fa",
    "padding": "4rem 1rem 2rem"
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "margin-top": "0rem",
    "margin-left": "20rem",
}

# make the sidebar
sidebar = html.Div(
    [html.H3("This is an example of a title"),
    html.Hr(),
    html.H6("This is a smaller title introducing the dropdown"),
    dcc.Dropdown(
    id='Fuel',
    value=df.Fuel_Type.unique(),
    options = [{'label': x, 'value': x} for x in df.Fuel_Type.unique()],
    multi=True,
    optionHeight=75,
    style={"margin-bottom": "50px"})

    ],
    style=SIDEBAR_STYLE,
)

# make the content
content = html.Div([dcc.Graph(id='graph')], style=CONTENT_STYLE)

# update the layout
app.layout= html.Div([sidebar, content])



# any change to the input Fuel will call the update_figure function and return a figure with updated data
@app.callback(
    Output('graph', 'figure'),
    Input('Fuel', 'value'))
def update_figure(Fuel):
    filtered_df = df[df.Fuel_Type.isin(Fuel)]

    fig = px.scatter(filtered_df, x="Year", y="Selling_Price", color="Transmission", size_max=55)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)