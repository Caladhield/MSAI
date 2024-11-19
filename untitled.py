import pandas as pd

data = pd.read_csv('Exercise_1_Monthly_Temperature_Data.txt')
max_temp_index = data['Temperature'].idxmax()
min_temp_index = data['Temperature'].idxmin()

# Hämta raderna för högsta och lägsta temperatur
highest_temp = data.loc[max_temp_index]
lowest_temp = data.loc[min_temp_index]

print("Högsta temperatur:", highest_temp)
print("Lägsta temperatur:", lowest_temp)

data['Week'] = (data.index // 7) + 1

# Beräkna medeltemperatur för varje vecka
weekly_avg = data.groupby('Week')['Temperature'].mean()

print(weekly_avg)