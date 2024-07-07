#Suppose you want to track and analyze the monthly energy consumption in your home.
#You have recorded the monthly energy usage for electricity and gas over a year, and you want to represent this data using Pandas Series.
#Do analysis on data

import pandas as pd
energy_data = {
    'January': {'electricity': 300, 'gas': 50},
    'February': {'electricity': 280, 'gas': 55},
    'March': {'electricity': 310, 'gas': 60},
    'April': {'electricity': 290, 'gas': 58},
    'May': {'electricity': 280, 'gas': 56},
    'June': {'electricity': 270, 'gas': 52},
    'July': {'electricity': 260, 'gas': 51},
    'August': {'electricity': 270, 'gas': 53},
    'September': {'electricity': 280, 'gas': 55},
    'October': {'electricity': 300, 'gas': 58},
    'November': {'electricity': 310, 'gas': 60},
    'December': {'electricity': 320, 'gas': 62}
}

energy_df = pd.DataFrame(energy_data).transpose()


print("Monthly Energy Consumption Data:")
print(energy_df)

electricity_series = energy_df['electricity']
gas_series = energy_df['gas']

print("\nElectricity Consumption (kWh):")
print(electricity_series)

print("\nGas Consumption (therms):")
print(gas_series)

print("\nBasic Analysis:")
print(f"Total electricity consumed over the year: {electricity_series.sum()} kWh")
print(f"Total gas consumed over the year: {gas_series.sum()} therms")
print(f"Average monthly electricity consumption: {electricity_series.mean():.2f} kWh")
print(f"Average monthly gas consumption: {gas_series.mean():.2f} therms")
print(f"Maximum electricity consumption in a month: {electricity_series.max()} kWh (in {electricity_series.idxmax()})")
print(f"Maximum gas consumption in a month: {gas_series.max()} therms (in {gas_series.idxmax()})")
