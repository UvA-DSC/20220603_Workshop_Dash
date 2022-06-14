# Run this app with `python simple_app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("all_apps/appdata/car data.csv")

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph'),

    # add a dropdown that filters Fuel
    dcc.Dropdown(
    id='Fuel',
    value=df.Fuel_Type.unique(),
    options = [{'label': x, 'value': x} for x in df.Fuel_Type.unique()],
    multi=True,
    optionHeight=75,
    style={"margin-bottom": "50px"})
])

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