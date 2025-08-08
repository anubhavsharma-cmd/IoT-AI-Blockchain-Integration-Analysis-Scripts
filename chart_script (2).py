import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_csv("case_study_analysis.csv")

# Check the data structure
print("Data shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

# Define the color palette
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C', '#B4413C', '#964325', '#944454', '#13343B']

# Create scatter plot
fig = px.scatter(
    df, 
    x='Initial_Cost_Million_USD', 
    y='ROI_Percentage',
    size='Efficiency_Gain',
    color='Industry',
    title='Cost vs ROI Analysis',
    labels={
        'Initial_Cost_Million_USD': 'Init Cost ($M)',
        'ROI_Percentage': 'ROI (%)',
        'Efficiency_Gain': 'Efficiency',
        'Industry': 'Industry'
    },
    hover_data={
        'Initial_Cost_Million_USD': ':.1f',
        'ROI_Percentage': ':.1f', 
        'Efficiency_Gain': ':.1f',
        'Industry': True
    },
    color_discrete_sequence=colors
)

# Update traces with cliponaxis
fig.update_traces(
    cliponaxis=False,
    marker=dict(line=dict(width=1, color='white'))
)

# Center legend if 5 or fewer items
unique_industries = df['Industry'].nunique()
if unique_industries <= 5:
    fig.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5))

# Save the chart
fig.write_image("cost_roi_analysis.png")
print("Chart saved as cost_roi_analysis.png")