
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("airbnb_listings.csv")

# Show first few records
print("📄 Preview of Airbnb dataset:")
print(df[['name', 'neighbourhood_group', 'room_type', 'price']].head())

# Remove extreme prices for clarity
df = df[df['price'] < 500]

# Price distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], bins=50, color='coral')
plt.title("💰 Distribution of Airbnb Prices (Below $500)")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

# Average price by room type
plt.figure(figsize=(8, 4))
sns.barplot(data=df, x='room_type', y='price', ci=None, palette='Set2')
plt.title("🛏️ Average Price by Room Type")
plt.ylabel("Average Price ($)")
plt.show()

# Average price by neighborhood
top_neigh = df.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)
top_neigh.plot(kind='bar', color='skyblue', title="📍 Average Price by Neighborhood Group", figsize=(8, 4))
plt.ylabel("Price ($)")
plt.show()
