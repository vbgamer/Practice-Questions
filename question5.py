#Suppose you are managing a website and want to analyze the monthly revenue generated from advertising.
#You have recorded the monthly revenue for the past year,and you want to represent this data using a Pandas Series

import pandas as pd
revenue_data = [5000, 7000, 8000, 6000, 7500, 8500, 9000, 9500, 7000, 7200, 7800, 8000]

months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

revenue= pd.Series(revenue_data, index=months)
print("Monthly Revenue Data:")
print(revenue)
