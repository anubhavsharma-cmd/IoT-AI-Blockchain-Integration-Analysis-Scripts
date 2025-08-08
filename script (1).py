# Continue with detailed analysis
print("\n4. TECHNOLOGY INTEGRATION ANALYSIS BY INDUSTRY")
print("=" * 50)

industry_analysis = df.groupby('Industry').agg({
    'IoT_Integration_Level': ['mean', 'std'],
    'AI_Integration_Level': ['mean', 'std'],
    'Blockchain_Integration_Level': ['mean', 'std'],
    'Operational_Efficiency_Score': 'mean',
    'Cost_Reduction_Percentage': 'mean'
}).round(2)

print(industry_analysis)
print()

print("5. CORRELATION ANALYSIS")
print("=" * 50)
correlation_vars = ['IoT_Integration_Level', 'AI_Integration_Level', 'Blockchain_Integration_Level',
                   'Operational_Efficiency_Score', 'Cost_Reduction_Percentage', 'Security_Score',
                   'Data_Quality_Score', 'Technology_Synergy_Index']

correlation_matrix = df[correlation_vars].corr()
print("Correlation Matrix (Key Variables):")
print(correlation_matrix.round(3))
print()

# Statistical significance testing
print("6. STATISTICAL SIGNIFICANCE TESTS")
print("=" * 50)

# Test correlation between Technology Synergy Index and Operational Efficiency
correlation_coeff, p_value = stats.pearsonr(df['Technology_Synergy_Index'], df['Operational_Efficiency_Score'])
print(f"Technology Synergy Index vs Operational Efficiency:")
print(f"Correlation coefficient: {correlation_coeff:.4f}")
print(f"P-value: {p_value:.6f}")
print(f"Significance: {'Highly Significant' if p_value < 0.001 else 'Significant' if p_value < 0.05 else 'Not Significant'}")
print()

# Test correlation between Technology Synergy Index and Cost Reduction
correlation_coeff2, p_value2 = stats.pearsonr(df['Technology_Synergy_Index'], df['Cost_Reduction_Percentage'])
print(f"Technology Synergy Index vs Cost Reduction:")
print(f"Correlation coefficient: {correlation_coeff2:.4f}")
print(f"P-value: {p_value2:.6f}")
print(f"Significance: {'Highly Significant' if p_value2 < 0.001 else 'Significant' if p_value2 < 0.05 else 'Not Significant'}")
print()

print("7. REGRESSION ANALYSIS")
print("=" * 50)

# Multiple regression: Predict Operational Efficiency
X = df[['IoT_Integration_Level', 'AI_Integration_Level', 'Blockchain_Integration_Level']].values
y = df['Operational_Efficiency_Score'].values

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit regression model
model = LinearRegression()
model.fit(X_scaled, y)
y_pred = model.predict(X_scaled)

# Calculate metrics
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print("Multiple Linear Regression: Predicting Operational Efficiency")
print(f"R-squared: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"Model explains {r2*100:.1f}% of variance in operational efficiency")
print()

# Feature importance
feature_names = ['IoT Integration', 'AI Integration', 'Blockchain Integration']
coefficients = model.coef_
print("Feature Coefficients (standardized):")
for name, coef in zip(feature_names, coefficients):
    print(f"  {name}: {coef:.4f}")
print()

print("8. PERFORMANCE METRICS BY INTEGRATION LEVEL")
print("=" * 50)

# Categorize integration levels
df['IoT_Category'] = pd.cut(df['IoT_Integration_Level'], bins=[0, 33, 66, 100], labels=['Low', 'Medium', 'High'])
df['AI_Category'] = pd.cut(df['AI_Integration_Level'], bins=[0, 33, 66, 100], labels=['Low', 'Medium', 'High'])
df['Blockchain_Category'] = pd.cut(df['Blockchain_Integration_Level'], bins=[0, 33, 66, 100], labels=['Low', 'Medium', 'High'])

# Performance by IoT integration level
iot_performance = df.groupby('IoT_Category').agg({
    'Operational_Efficiency_Score': 'mean',
    'Cost_Reduction_Percentage': 'mean',
    'Security_Score': 'mean',
    'Response_Time_MS': 'mean'
}).round(2)

print("Performance by IoT Integration Level:")
print(iot_performance)
print()

# Performance by AI integration level
ai_performance = df.groupby('AI_Category').agg({
    'Operational_Efficiency_Score': 'mean',
    'Cost_Reduction_Percentage': 'mean',
    'Security_Score': 'mean',
    'Data_Quality_Score': 'mean'
}).round(2)

print("Performance by AI Integration Level:")
print(ai_performance)
print()

# Performance by Blockchain integration level
blockchain_performance = df.groupby('Blockchain_Category').agg({
    'Operational_Efficiency_Score': 'mean',
    'Cost_Reduction_Percentage': 'mean',
    'Security_Score': 'mean',
    'Data_Quality_Score': 'mean'
}).round(2)

print("Performance by Blockchain Integration Level:")
print(blockchain_performance)
print()