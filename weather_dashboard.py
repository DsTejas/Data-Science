import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("weather_data.csv")

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Preview
print(df.head())

# Group by day
daily_summary = df.groupby('date').agg({
    'temperature': 'mean',
    'humidity': 'mean',
    'wind_speed': 'mean'
}).reset_index()

print("\n Daily Summary:")
print(daily_summary.head())

# Line plot for temperature
plt.figure(figsize=(10, 5))
sns.lineplot(data=daily_summary, x='date', y='temperature', marker='o', color='orangered')
plt.title("🌡 Daily Average Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Line plot for humidity
plt.figure(figsize=(10, 5))
sns.lineplot(data=daily_summary, x='date', y='humidity', marker='o', color='blue')
plt.title("💧 Daily Average Humidity")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Wind speed plot
plt.figure(figsize=(10, 5))
sns.barplot(data=daily_summary, x='date', y='wind_speed', palette='Blues_r')
plt.title(" Wind Speed Per Day")
plt.xlabel("Date")
plt.ylabel("Wind Speed (km/h)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
