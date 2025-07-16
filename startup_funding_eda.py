import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("startup_funding.csv")

# Clean data
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date', 'CityLocation', 'IndustryVertical', 'AmountInUSD'], inplace=True)

# Yearly funding trend
df['Year'] = df['Date'].dt.year
funding_by_year = df.groupby('Year')['AmountInUSD'].sum()

# Plot funding by year
plt.figure(figsize=(10, 5))
funding_by_year.plot(kind='bar', color='teal')
plt.title(" Total Startup Funding in India (Year-wise)")
plt.xlabel("Year")
plt.ylabel("Funding (in USD)")
plt.tight_layout()
plt.show()

# Top cities
top_cities = df['CityLocation'].value_counts().head(10)
sns.barplot(y=top_cities.index, x=top_cities.values, palette='viridis')
plt.title(" Top 10 Cities by Number of Funded Startups")
plt.xlabel("Number of Startups")
plt.ylabel("City")
plt.tight_layout()
plt.show()
