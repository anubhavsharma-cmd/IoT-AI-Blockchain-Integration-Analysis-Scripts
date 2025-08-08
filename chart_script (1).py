import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Load the data
df = pd.read_csv('iot_ai_blockchain_analysis.csv')

# Create 3-month intervals for Project_Duration_Months
df['Duration_Interval'] = ((df['Project_Duration_Months'] // 3) * 3).astype(int)

# Group by 3-month intervals and calculate statistics
grouped = df.groupby('Duration_Interval').agg({
    'Operational_Efficiency_Score': ['mean', 'std', 'count']
}).round(2)

# Flatten column names
grouped.columns = ['_'.join(col).strip() for col in grouped.columns]
grouped = grouped.reset_index()

# Calculate confidence intervals (95%)
grouped['ci'] = 1.96 * grouped['Operational_Efficiency_Score_std'] / np.sqrt(grouped['Operational_Efficiency_Score_count'])
grouped['upper'] = grouped['Operational_Efficiency_Score_mean'] + grouped['ci']
grouped['lower'] = grouped['Operational_Efficiency_Score_mean'] - grouped['ci']

# Create the line chart with error bars
fig = go.Figure()

# Add the main line with error bars
fig.add_trace(go.Scatter(
    x=grouped['Duration_Interval'],
    y=grouped['Operational_Efficiency_Score_mean'],
    error_y=dict(
        type='data',
        array=grouped['ci'],
        visible=True
    ),
    mode='lines+markers',
    name='Efficiency',
    line=dict(color='#1FB8CD', width=3),
    marker=dict(size=8, color='#1FB8CD'),
    cliponaxis=False
))

# Update layout
fig.update_layout(
    title='Efficiency vs Project Duration'
)

# Update axes with abbreviated labels
fig.update_xaxes(title='Duration (mo)')
fig.update_yaxes(title='Efficiency')

# Add hover template
fig.update_traces(
    hovertemplate='<b>Duration:</b> %{x} months<br>' +
                  '<b>Efficiency:</b> %{y:.1f}<br>' +
                  '<extra></extra>'
)

# Save the chart
fig.write_image('efficiency_duration_chart.png')