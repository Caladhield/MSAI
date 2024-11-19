import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Exercise_3_Regional_Sales_Data.txt')
total_sales = data['Sales'].sum()
best_region = data.loc[data['Sales'].idxmax(), 'Region']
print(f"Region with highest sales: {best_region}")
print(f"Total sales: {total_sales}")

# Skapa ett stapeldiagram
plt.figure(figsize=(5, 5))
plt.bar(data['Region'], data['Sales'], color='teal')

# Lägg till etiketter och titel
plt.title('Sales per region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Sales', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Markera region med högsta försäljning
plt.text(
    data['Region'][data['Sales'].idxmax()], 
    data['Sales'].max(), 
    f"{data['Sales'].max()}",
    ha='center',
    fontsize=10,
)

plt.show()