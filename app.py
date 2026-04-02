import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Initialize app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    style={'font-family': 'Arial, sans-serif', 'backgroundColor': '#f9f9f9', 'padding': '20px'},
    children=[
        html.H1(
            "Soul Foods Sales Visualiser",
            style={'textAlign': 'center', 'color': '#2c3e50'}
        ),

        html.Div(
            [
                html.Label("Select Region:", style={'font-weight': 'bold', 'margin-right': '10px'}),
                dcc.RadioItems(
                    id='region-selector',
                    options=[
                        {'label': 'All', 'value': 'all'},
                        {'label': 'North', 'value': 'north'},
                        {'label': 'East', 'value': 'east'},
                        {'label': 'South', 'value': 'south'},
                        {'label': 'West', 'value': 'west'}
                    ],
                    value='all',
                    labelStyle={'display': 'inline-block', 'margin-right': '15px', 'color': '#34495e'}
                )
            ],
            style={'textAlign': 'center', 'margin-bottom': '20px'}
        ),

        dcc.Graph(id='sales-line-chart')
    ]
)

# Callback to update chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-selector', 'value')]
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f"Sales of Pink Morsels ({selected_region.title()})",
        labels={'date': 'Date', 'sales': 'Sales'}
    )

    fig.update_layout(
        plot_bgcolor='#ecf0f1',
        paper_bgcolor='#f9f9f9',
        font_color='#2c3e50'
    )

    return fig

# Run app
if __name__ == '__main__':
    app.run(debug=True)