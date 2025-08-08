import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Load the data
df = pd.read_csv('iot_ai_blockchain_analysis.csv')

# Create correlation heatmap of key variables
key_variables = ['IoT_Integration_Level', 'AI_Integration_Level', 'Blockchain_Integration_Level', 
                'Operational_Efficiency_Score', 'Cost_Reduction_Percentage', 'Security_Score']

# Calculate correlation matrix
corr_matrix = df[key_variables].corr()

# Create abbreviated column names for the 15 character limit
abbreviated_vars = ['IoT Intgr', 'AI Intgr', 'Blockchain', 'Op Effcy', 'Cost Reduct', 'Security']

# Create the heatmap
fig = px.imshow(
    corr_matrix.values,
    x=abbreviated_vars,
    y=abbreviated_vars,
    color_continuous_scale=['#DB4545', '#D2BA4C', '#2E8B57'],
    aspect='auto',
    title='Tech Integration Correlations'
)

# Update layout
fig.update_layout(
    xaxis_title='',
    yaxis_title='',
    coloraxis_colorbar=dict(title='Correlation')
)

# Add correlation values as text annotations
for i in range(len(abbreviated_vars)):
    for j in range(len(abbreviated_vars)):
        correlation_value = corr_matrix.iloc[i, j]
        fig.add_annotation(
            x=j, y=i,
            text=f"{correlation_value:.2f}",
            showarrow=False,
            font=dict(color="white" if abs(correlation_value) > 0.5 else "black", size=12)
        )

# Save the chart
fig.write_image('tech_correlation_heatmap.png')
print("Correlation heatmap saved as tech_correlation_heatmap.png")