import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# ---------- Load and clean the data ----------
df = pd.read_csv('formatted_output.csv')

# Force lowercase column names
df.columns = df.columns.str.lower()

# Clean the sales column (remove $ and commas, convert to float)
df['sales'] = df['sales'].replace(r'[\$,]', '', regex=True).astype(float)

# Clean region names (remove extra spaces)
df['region'] = df['region'].str.strip()

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Debug: print to terminal so you can see it's working
print("✅ Data loaded successfully!")
print(f"Total rows: {len(df)}")
print(f"Regions found: {df['region'].unique().tolist()}")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")

# ---------- Initialize the Dash app ----------
app = Dash(__name__)

# Get unique region list for dropdown
region_options = [{'label': r, 'value': r} for r in df['region'].unique()]

# ---------- Layout ----------
app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis", style={'textAlign': 'center'}),
    
    html.Label("Select Region(s):", style={'fontWeight': 'bold'}),
    dcc.Dropdown(
        id='region-dropdown',
        options=region_options,
        value=df['region'].unique().tolist(),  # Select all by default
        multi=True,
        style={'width': '50%'}
    ),
    
    dcc.Graph(id='sales-graph'),
    
    html.Div(id='summary-text', style={'marginTop': '20px', 'fontSize': '18px'})
])

# ---------- Callback ----------
@app.callback(
    [Output('sales-graph', 'figure'),
     Output('summary-text', 'children')],
    [Input('region-dropdown', 'value')]
)
def update_graph(selected_regions):
    # If no regions selected, return empty figure
    if not selected_regions:
        return px.line(title="Select at least one region"), "Please select a region."
    
    # Filter data
    filtered_df = df[df['region'].isin(selected_regions)]
    
    # Group by date to sum sales
    daily_sales = filtered_df.groupby('date', as_index=False)['sales'].sum()
    
    # Create the line chart
    fig = px.line(
        daily_sales, 
        x='date', 
        y='sales',
        title='Total Daily Sales of Pink Morsels',
        labels={'date': 'Date', 'sales': 'Total Sales ($)'}
    )
    
    # Add vertical line for price increase
    fig.add_vline(
        x=pd.Timestamp('2021-01-15'), 
        line_dash="dash", 
        line_color="red",
        annotation_text="💰 Price Increase",
        annotation_position="top"
    )
    
    # Calculate averages
    before = daily_sales[daily_sales['date'] < '2021-01-15']['sales'].mean()
    after = daily_sales[daily_sales['date'] >= '2021-01-15']['sales'].mean()
    
    if pd.isna(before) or pd.isna(after):
        summary = "Not enough data to compare."
    elif after > before:
        summary = f"📈 Sales HIGHER after price increase (Avg before: ${before:,.2f} | Avg after: ${after:,.2f})"
    else:
        summary = f"📉 Sales LOWER after price increase (Avg before: ${before:,.2f} | Avg after: ${after:,.2f})"
    
    return fig, summary

# ---------- Run ----------
if __name__ == '__main__':
    app.run(debug=True)