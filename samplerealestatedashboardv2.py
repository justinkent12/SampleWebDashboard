import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data (replace this with your own real estate data)
data = {
    'Location': ['City A', 'City B', 'City C', 'City D'],
    'Average Price': [500000, 750000, 600000, 800000],
    'Listings': [150, 300, 250, 200]
}
df = pd.DataFrame(data)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Real Estate Dashboard"),
    
    # Dropdown filter for locations
    html.Label("Select Location:"),
    dcc.Dropdown(
        id="location-dropdown",
        options=[{'label': loc, 'value': loc} for loc in df['Location'].unique()],
        multi=True
    ),
    
    # Graph for average prices
    dcc.Graph(id="price-trend"),
    
    # Graph for number of listings
    dcc.Graph(id="listings-bar")
])

# Callback for updating the graphs based on location
@app.callback(
    [Output("price-trend", "figure"), Output("listings-bar", "figure")],
    [Input("location-dropdown", "value")]
)
def update_graphs(selected_locations):
    filtered_df = df[df['Location'].isin(selected_locations)] if selected_locations else df
    
    # Average price trend line chart
    fig_price = px.line(filtered_df, x="Location", y="Average Price", title="Average Price by Location", markers=True,text="Average Price")
    fig_price.update_layout(
        plot_bgcolor='white'
    )


    # Listings bar chart
    fig_listings = px.line(filtered_df, x="Location", y="Listings", title="Number of Listings by Location",text="Listings",markers=True)
    fig_listings.update_layout(
        plot_bgcolor='white'
    )


    return fig_price, fig_listings

if __name__ == "__main__":
    app.run_server(debug=True)
