
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("spotify_tracks.csv")  # replace with your path

# Preview the data
print("🎧 Dataset preview:")
print(df.head())

# Summary statistics
print("\n📊 Dataset Summary:")
print(df.describe())

# Correlation heatmap of numerical audio features
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='YlGnBu')
plt.title("🎶 Correlation Between Audio Features")
plt.show()

# Top 10 most energetic songs
top_energy = df[['track_name', 'artists', 'energy']].sort_values(by='energy', ascending=False).head(10)
print("\n🔥 Top 10 Energetic Tracks:")
print(top_energy)

# Danceability vs Energy
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='danceability', y='energy', alpha=0.6)
plt.title("💃 Danceability vs Energy")
plt.xlabel("Danceability")
plt.ylabel("Energy")
plt.grid(True)
plt.show()
