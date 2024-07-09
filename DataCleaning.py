import pandas as pd

data = pd.read_csv('country_profile_variables.csv')
# Convert columns to numeric
for col in data.columns[2:]:
    data[col] = pd.to_numeric(data[col], errors='coerce')

