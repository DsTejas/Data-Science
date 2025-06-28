import pandas as pd

# Load the global COVID-19 dataset from an open data source
data_url = 'https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv'
df = pd.read_csv(data_url)

# Display the first few rows to understand the structure of the data
print("📌 Dataset preview:")
print(df.head())

# Filter the dataset to only include India's data
india_data = df[df['Country'] == 'India'].copy()

# Create a new column to calculate active cases
india_data['Active'] = india_data['Confirmed'] - india_data['Recovered'] - india_data['Deaths']

# Print some basic statistics about the Indian dataset
print("\n📊 Summary of India's COVID-19 data:")
print(india_data.describe())

# Calculate daily new confirmed cases using the diff() method
india_data['New Cases'] = india_data['Confirmed'].diff()

# Find the day with the highest number of new confirmed cases
peak_day = india_data.loc[india_data['New Cases'].idxmax()]

# Output the result clearly
print("\n📈 Day with the highest number of new cases in India:")
print(peak_day[['Date', 'New Cases']])
