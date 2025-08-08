import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# Create comprehensive synthetic dataset based on real IoT, AI, and Blockchain integration in operations management
np.random.seed(42)

# Generate dataset with realistic operational metrics
n_samples = 1000

# Company characteristics
companies = ['ManufacturingCorp A', 'TechSolutions B', 'LogisticsPro C', 'HealthcarePlus D', 'RetailChain E', 
             'EnergyGrid F', 'AgriSmart G', 'FinanceSecure H', 'AutoMotive I', 'FoodTrack J']

company_types = ['Manufacturing', 'Technology', 'Logistics', 'Healthcare', 'Retail', 
                'Energy', 'Agriculture', 'Finance', 'Automotive', 'Food & Beverage']

# Technology integration levels (0-1 scale)
iot_integration = np.random.beta(2, 3, n_samples)
ai_integration = np.random.beta(2.5, 2.5, n_samples)
blockchain_integration = np.random.beta(1.5, 4, n_samples)

# Calculate synergy effect (multiplicative interaction)
synergy_factor = (iot_integration * ai_integration * blockchain_integration) ** 0.5

# Operational metrics with realistic correlations
operational_efficiency = 60 + 30 * synergy_factor + np.random.normal(0, 5, n_samples)
operational_efficiency = np.clip(operational_efficiency, 40, 100)

cost_reduction = 5 + 35 * synergy_factor + np.random.normal(0, 8, n_samples)
cost_reduction = np.clip(cost_reduction, 0, 50)

security_score = 65 + 25 * blockchain_integration + 10 * ai_integration + np.random.normal(0, 6, n_samples)
security_score = np.clip(security_score, 50, 100)

data_quality = 70 + 20 * blockchain_integration + 15 * ai_integration + np.random.normal(0, 5, n_samples)
data_quality = np.clip(data_quality, 60, 100)

response_time = 500 - 300 * iot_integration - 150 * ai_integration + np.random.normal(0, 50, n_samples)
response_time = np.clip(response_time, 50, 600)

# Create DataFrame
data = {
    'Company': np.random.choice(companies, n_samples),
    'Industry': np.random.choice(company_types, n_samples),
    'IoT_Integration_Level': np.round(iot_integration * 100, 1),
    'AI_Integration_Level': np.round(ai_integration * 100, 1),
    'Blockchain_Integration_Level': np.round(blockchain_integration * 100, 1),
    'Operational_Efficiency_Score': np.round(operational_efficiency, 1),
    'Cost_Reduction_Percentage': np.round(cost_reduction, 1),
    'Security_Score': np.round(security_score, 1),
    'Data_Quality_Score': np.round(data_quality, 1),
    'Response_Time_MS': np.round(response_time, 0),
    'Project_Duration_Months': np.random.randint(6, 36, n_samples),
    'Implementation_Cost_K': np.random.randint(100, 2000, n_samples)
}

df = pd.DataFrame(data)

# Calculate derived metrics
df['Technology_Synergy_Index'] = np.round((df['IoT_Integration_Level'] * 
                                         df['AI_Integration_Level'] * 
                                         df['Blockchain_Integration_Level']) ** (1/3), 1)

df['ROI_Score'] = np.round((df['Cost_Reduction_Percentage'] * df['Operational_Efficiency_Score']) / 
                          (df['Implementation_Cost_K'] / 100), 1)

print("=== IoT, AI, and Blockchain Integration in Operations Management ===")
print("=== Comprehensive Data Analysis Report ===\n")

print("1. DATASET OVERVIEW")
print("=" * 50)
print(f"Total Records: {len(df)}")
print(f"Companies Analyzed: {df['Company'].nunique()}")
print(f"Industries Covered: {df['Industry'].nunique()}")
print(f"Time Period: {df['Project_Duration_Months'].min()}-{df['Project_Duration_Months'].max()} months")
print()

print("2. DESCRIPTIVE STATISTICS")
print("=" * 50)
key_metrics = ['IoT_Integration_Level', 'AI_Integration_Level', 'Blockchain_Integration_Level',
               'Operational_Efficiency_Score', 'Cost_Reduction_Percentage', 'Security_Score']

desc_stats = df[key_metrics].describe()
print(desc_stats.round(2))
print()

# Display first 10 rows as sample
print("3. SAMPLE DATA")
print("=" * 50)
print(df.head(10).to_string(index=False))
print("\n... (showing first 10 of 1000 records)")