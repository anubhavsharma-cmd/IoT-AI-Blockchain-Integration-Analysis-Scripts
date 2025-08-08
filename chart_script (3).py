import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Create sample ROI timeline data for 36 months
months = list(range(1, 37))

# Simulate realistic ROI progression - starts negative, reaches break-even, then positive
# Initial investment costs, then gradual returns
cumulative_roi = []
initial_investment = -500000  # $500k initial investment
monthly_benefit = 25000       # $25k monthly benefit after ramp-up
ramp_up_months = 6           # 6 months to reach full benefit

current_roi = initial_investment
for month in months:
    if month <= ramp_up_months:
        # Ramp-up period with gradual benefit increase
        monthly_return = monthly_benefit * (month / ramp_up_months) - 10000  # Some ongoing costs
    else:
        # Full benefits minus ongoing costs
        monthly_return = monthly_benefit - 8000
    
    current_roi += monthly_return
    cumulative_roi.append(current_roi)

# Find break-even point
break_even_month = None
break_even_roi = None
for i, roi in enumerate(cumulative_roi):
    if roi >= 0:
        break_even_month = months[i]
        break_even_roi = roi
        break
        
# If no break-even found, interpolate
if break_even_month is None and len(cumulative_roi) > 1:
    for i in range(len(cumulative_roi) - 1):
        if cumulative_roi[i] < 0 and cumulative_roi[i + 1] > 0:
            # Linear interpolation to find exact break-even point
            ratio = -cumulative_roi[i] / (cumulative_roi[i + 1] - cumulative_roi[i])
            break_even_month = months[i] + ratio
            break_even_roi = 0
            break

# Create the line chart
fig = go.Figure()

# Add ROI line
fig.add_trace(go.Scatter(
    x=months,
    y=cumulative_roi,
    mode='lines+markers',
    name='Cumulative ROI',
    line=dict(color='#2E8B57', width=3),
    marker=dict(size=6),
    hovertemplate='Month: %{x}<br>ROI: $%{y:,.0f}<extra></extra>'
))

# Add break-even point if found
if break_even_month is not None:
    fig.add_trace(go.Scatter(
        x=[break_even_month],
        y=[break_even_roi],
        mode='markers',
        name='Break-even',
        marker=dict(
            color='#DB4545',
            size=12,
            symbol='diamond'
        ),
        hovertemplate='Break-even<br>Month: %{x:.1f}<br>ROI: $%{y:,.0f}<extra></extra>'
    ))

# Add zero line for reference
fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)

# Format the chart
fig.update_layout(
    title='ROI Timeline - 36 Month Projection',
    xaxis_title='Month',
    yaxis_title='Cumulative ROI ($)',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Format axes - removed cliponaxis as it's not valid
fig.update_yaxes(tickformat='$,.0f')

# Save the chart
fig.write_image('roi_timeline_chart.png')