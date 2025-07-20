import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("earthquake_data.csv")

# Preview
print(df.head())

# Convert time column to datetime
df['time'] = pd.to_datetime(df['time'])

# Extract year and month
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month

# Plot: Earthquakes per year
plt.figure(figsize=(10, 5))
df['year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title("📅 Number of Earthquakes per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Plot: Magnitude Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['mag'], bins=30, kde=True, color='tomato')
plt.title("🌋 Earthquake Magnitude Distribution")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Plot: Depth vs Magnitude
plt.figure(figsize=(7, 5))
sns.scatterplot(x='depth', y='mag', data=df, hue='mag', palette='coolwarm', size='mag', sizes=(20, 200))
plt.title("⛏️ Earthquake Depth vs Magnitude")
plt.xlabel("Depth (km)")
plt.ylabel("Magnitude")
plt.tight_layout()
plt.show()

# Top 10 countries (or places) with most earthquakes
top_places = df['place'].dropna().apply(lambda x: x.split(",")[-1].strip()).value_counts().head(10)

plt.figure(figsize=(9, 5))
sns.barplot(x=top_places.values, y=top_places.index, palette='magma')
plt.title("🌐 Top 10 Most Affected Countries/Regions")
plt.xlabel("Number of Earthquakes")
plt.ylabel("Region")
plt.tight_layout()
plt.show()
