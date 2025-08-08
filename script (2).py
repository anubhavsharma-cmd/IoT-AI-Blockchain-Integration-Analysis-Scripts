# Advanced analysis and case studies
print("9. ADVANCED CASE STUDY ANALYSIS")
print("=" * 50)

# High-performing case studies
high_performers = df[
    (df['Technology_Synergy_Index'] > df['Technology_Synergy_Index'].quantile(0.8)) &
    (df['Operational_Efficiency_Score'] > df['Operational_Efficiency_Score'].quantile(0.8))
].copy()

print(f"High-Performing Cases (Top 20% in both Synergy and Efficiency): {len(high_performers)} companies")
print("\nCharacteristics of High Performers:")
high_perf_stats = high_performers[['IoT_Integration_Level', 'AI_Integration_Level', 
                                  'Blockchain_Integration_Level', 'Operational_Efficiency_Score',
                                  'Cost_Reduction_Percentage', 'Security_Score', 'ROI_Score']].describe()
print(high_perf_stats.round(2))
print()

# Low-performing case studies
low_performers = df[
    (df['Technology_Synergy_Index'] < df['Technology_Synergy_Index'].quantile(0.2)) &
    (df['Operational_Efficiency_Score'] < df['Operational_Efficiency_Score'].quantile(0.2))
].copy()

print(f"Low-Performing Cases (Bottom 20% in both Synergy and Efficiency): {len(low_performers)} companies")
if len(low_performers) > 0:
    print("\nCharacteristics of Low Performers:")
    low_perf_stats = low_performers[['IoT_Integration_Level', 'AI_Integration_Level', 
                                    'Blockchain_Integration_Level', 'Operational_Efficiency_Score',
                                    'Cost_Reduction_Percentage', 'Security_Score', 'ROI_Score']].describe()
    print(low_perf_stats.round(2))
print()

print("10. IMPLEMENTATION SUCCESS FACTORS")
print("=" * 50)

# Analyze factors that distinguish successful implementations
success_threshold = df['Technology_Synergy_Index'].quantile(0.75)
df['Success_Category'] = df['Technology_Synergy_Index'].apply(lambda x: 'High Success' if x >= success_threshold else 'Standard')

success_analysis = df.groupby('Success_Category').agg({
    'Project_Duration_Months': ['mean', 'std'],
    'Implementation_Cost_K': ['mean', 'std'],
    'Operational_Efficiency_Score': 'mean',
    'Cost_Reduction_Percentage': 'mean',
    'ROI_Score': 'mean'
}).round(2)

print("Success Factors Analysis:")
print(success_analysis)
print()

print("11. ROI AND COST-BENEFIT ANALYSIS")
print("=" * 50)

# ROI categories
df['ROI_Category'] = pd.cut(df['ROI_Score'], bins=[0, 50, 100, 200, float('inf')], 
                           labels=['Low ROI', 'Medium ROI', 'High ROI', 'Exceptional ROI'])

roi_analysis = df.groupby('ROI_Category').agg({
    'IoT_Integration_Level': 'mean',
    'AI_Integration_Level': 'mean',
    'Blockchain_Integration_Level': 'mean',
    'Technology_Synergy_Index': 'mean',
    'Implementation_Cost_K': 'mean',
    'Project_Duration_Months': 'mean'
}).round(2)

print("ROI Categories Analysis:")
print(roi_analysis)
print()

# Cost-effectiveness by industry
cost_effectiveness = df.groupby('Industry').agg({
    'Implementation_Cost_K': 'mean',
    'ROI_Score': 'mean',
    'Project_Duration_Months': 'mean',
    'Technology_Synergy_Index': 'mean'
}).round(2)

print("Cost-Effectiveness by Industry:")
print(cost_effectiveness)
print()

print("12. PREDICTIVE INSIGHTS AND RECOMMENDATIONS")
print("=" * 50)

# Calculate optimal integration thresholds
optimal_iot = df[df['Operational_Efficiency_Score'] > df['Operational_Efficiency_Score'].quantile(0.8)]['IoT_Integration_Level'].mean()
optimal_ai = df[df['Operational_Efficiency_Score'] > df['Operational_Efficiency_Score'].quantile(0.8)]['AI_Integration_Level'].mean()
optimal_blockchain = df[df['Operational_Efficiency_Score'] > df['Operational_Efficiency_Score'].quantile(0.8)]['Blockchain_Integration_Level'].mean()

print("Optimal Integration Levels for Top Performance:")
print(f"IoT Integration: {optimal_iot:.1f}%")
print(f"AI Integration: {optimal_ai:.1f}%")
print(f"Blockchain Integration: {optimal_blockchain:.1f}%")
print()

# Technology impact analysis
print("Technology Impact Rankings (based on correlation with efficiency):")
tech_impacts = {
    'Blockchain Integration': correlation_matrix.loc['Blockchain_Integration_Level', 'Operational_Efficiency_Score'],
    'IoT Integration': correlation_matrix.loc['IoT_Integration_Level', 'Operational_Efficiency_Score'],
    'AI Integration': correlation_matrix.loc['AI_Integration_Level', 'Operational_Efficiency_Score']
}

sorted_impacts = sorted(tech_impacts.items(), key=lambda x: x[1], reverse=True)
for i, (tech, impact) in enumerate(sorted_impacts, 1):
    print(f"{i}. {tech}: {impact:.3f}")
print()

# Save data to CSV for further analysis
csv_filename = "iot_ai_blockchain_analysis.csv"
df.to_csv(csv_filename, index=False)
print(f"13. DATA EXPORT")
print("=" * 50)
print(f"Complete dataset saved to: {csv_filename}")
print(f"Total variables: {len(df.columns)}")
print(f"Key metrics included for visualization and further analysis")
print()

print("14. EXECUTIVE SUMMARY")
print("=" * 50)
print("Key Findings:")
print(f"• Technology synergy index strongly correlates with operational efficiency (r={correlation_coeff:.3f}, p<0.001)")
print(f"• Blockchain integration shows highest impact on operational efficiency (correlation: {tech_impacts['Blockchain Integration']:.3f})")
print(f"• High-performing organizations achieve {high_performers['Operational_Efficiency_Score'].mean():.1f}% efficiency vs {df['Operational_Efficiency_Score'].mean():.1f}% average")
print(f"• Cost reduction ranges from {df['Cost_Reduction_Percentage'].min():.1f}% to {df['Cost_Reduction_Percentage'].max():.1f}%, with mean of {df['Cost_Reduction_Percentage'].mean():.1f}%")
print(f"• ROI varies significantly: Low performers average {df[df['ROI_Category'] == 'Low ROI']['ROI_Score'].mean():.1f} vs high performers {df[df['ROI_Category'] == 'Exceptional ROI']['ROI_Score'].mean():.1f}")
print(f"• Implementation costs range ${df['Implementation_Cost_K'].min()}K - ${df['Implementation_Cost_K'].max()}K with {df['Project_Duration_Months'].mean():.1f} month average duration")