import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Exercise_1_Monthly_Temperature_Data.txt')
max_temp_index = data['Temperature'].idxmax()
min_temp_index = data['Temperature'].idxmin()

highest_temp = data.loc[max_temp_index]
lowest_temp = data.loc[min_temp_index]

print("Högsta temperatur:", highest_temp)
print("Lägsta temperatur:", lowest_temp)

data['Week'] = (data.index // 7) + 1

weekly_avg = data.groupby('Week')['Temperature'].mean()

print(weekly_avg)


plt.figure(figsize=(12, 6))
plt.plot(data['Temperature'], label='Temperatur över tid', color='blue')


plt.scatter(max_temp_index, highest_temp['Temperature'], color='red', label='Högsta temperatur', zorder=5)
plt.scatter(min_temp_index, lowest_temp['Temperature'], color='green', label='Lägsta temperatur', zorder=5)


plt.title('Dagliga temperaturer', fontsize=16)
plt.xlabel('Dag', fontsize=12)
plt.ylabel('Temperatur', fontsize=12)
plt.legend()
plt.grid()
plt.show()