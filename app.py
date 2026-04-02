import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("formatted_output.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig = px.line(df, x="date", y="sales", title="Sales of Pink Morsels Over Time")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)