import pandas as pd
import matplotlib.pyplot as plt

# Sample AQI data
data = {
    'City': ['Delhi', 'Mumbai', 'Kolkata', 'Bangalore', 'Chennai', 'Hyderabad', 'Ahmedabad'],
    'AQI': [340, 180, 250, 90, 130, 170, 310]
}

df = pd.DataFrame(data)

# Categorize AQI values
def categorize_aqi(aqi):
    if aqi <= 100:
        return 'Good'
    elif aqi <= 200:
        return 'Moderate'
    elif aqi <= 300:
        return 'Poor'
    else:
        return 'Very Poor'

df['Category'] = df['AQI'].apply(categorize_aqi)

# Assign colors based on category
color_map = {
    'Good': 'green',
    'Moderate': 'yellow',
    'Poor': 'orange',
    'Very Poor': 'red'
}
colors = df['Category'].map(color_map)

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['City'], df['AQI'], color=colors)
plt.title(" Air Quality Index by City")
plt.xlabel("City")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()

# Display category labels
for index, value in enumerate(df['AQI']):
    plt.text(index, value + 10, df['Category'][index], ha='center', fontsize=9)

plt.show()
