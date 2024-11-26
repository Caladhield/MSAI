import pandas as pd
import matplotlib.pyplot as plt

# Läs in data (exempeldata, byt ut med din egen fil)
data = pd.read_csv('Exercise_1_Monthly_Temperature_Data.txt')  # Se till att filen har en kolumn för temperatur

# Beräkna genomsnitt och standardavvikelse
mean_temp = data['Temperature'].mean()
stanard_temp = data['Temperature'].std()

# Identifiera avvikelser
threshold_upper = mean_temp + 2 * stanard_temp
threshold_lower = mean_temp - 2 * stanard_temp
outliers = (data['Temperature'] > threshold_upper) | (data['Temperature'] < threshold_lower)

# Skapa scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data.index, data['Temperature'], label='Temperatur', color='blue', alpha=0.7)
plt.scatter(data.index[outliers], data['Temperature'][outliers], label='Avvikelser', color='red', alpha=0.7)
plt.axhline(mean_temp, color='green', linestyle='--', label='Genomsnitt')
plt.xlabel('Index')
plt.ylabel('Temperatur')
plt.title('Scatter Plot med Avvikelser Markerade')
plt.legend()
plt.show()
