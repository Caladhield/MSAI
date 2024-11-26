import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load the file
# Manually creating the dataframe from your input
data = pd.DataFrame({
    'Region': ['Norr', 'Syd', 'Öst', 'Väst'],
    'Sales': [12000, 15000, 8000, 10000]
})

# 2. Simulate monthly data
np.random.seed(42)
months = 12
regions = data['Region'].unique()
monthly_data = []

for region in regions:
    base_sales = data.loc[data['Region'] == region, 'Sales'].values[0]
    sales_over_time = base_sales * (1 + 0.05 * np.random.randn(months))  # Simulate variation
    for month, sales in enumerate(sales_over_time, start=1):
        monthly_data.append({'Region': region, 'Month': month, 'Sales': sales})

monthly_df = pd.DataFrame(monthly_data)

# 3. Create line chart
plt.figure(figsize=(12, 6))
for region in regions:
    region_data = monthly_df[monthly_df['Region'] == region]
    plt.plot(region_data['Month'], region_data['Sales'], label=region)
    
plt.title('Försäljningens utveckling över tid per region')
plt.xlabel('Månad')
plt.ylabel('Försäljning')
plt.legend()
plt.grid(True)
plt.show()

# 4. Forecast sales for next month using linear regression
projections = {}
for region in regions:
    region_data = monthly_df[monthly_df['Region'] == region]
    X = region_data['Month'].values.reshape(-1, 1)
    y = region_data['Sales'].values
    model = LinearRegression()
    model.fit(X, y)
    next_month = months + 1
    prediction = model.predict([[next_month]])
    projections[region] = prediction[0]

    print(f"Prognos för nästa månad ({region}): {prediction[0]:.2f}")

# 5. Identify the fastest growing region
growth_rates = {}
for region in regions:
    region_data = monthly_df[monthly_df['Region'] == region]
    X = region_data['Month'].values.reshape(-1, 1)
    y = region_data['Sales'].values
    model = LinearRegression()
    model.fit(X, y)
    growth_rates[region] = model.coef_[0]  # Coefficient represents growth rate

fastest_growing_region = max(growth_rates, key=growth_rates.get)
print(f"Regionen med snabbast tillväxttakt: {fastest_growing_region} (Tillväxt: {growth_rates[fastest_growing_region]:.2f})")
