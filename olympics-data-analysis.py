import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("athlete_events.csv")

# Preview
print("📄 Dataset Preview:")
print(df[['Name', 'Sex', 'Age', 'Team', 'Sport', 'Medal']].head())

# Gender participation over the years
gender_df = df.groupby(['Year', 'Sex'])['ID'].count().reset_index()
sns.lineplot(data=gender_df, x='Year', y='ID', hue='Sex')
plt.title("👨‍🦰 vs 👩‍🦰 Gender Participation Over Time")
plt.ylabel("Number of Athletes")
plt.grid(True)
plt.show()

# Most successful countries
medal_df = df.dropna(subset=['Medal'])
top_countries = medal_df['Team'].value_counts().head(10)
print("\n🏆 Top 10 Countries by Medals:\n", top_countries)

# Medal count by sport
top_sports = medal_df['Sport'].value_counts().head(10)
top_sports.plot(kind='bar', color='orange')
plt.title("🥇 Top 10 Sports by Medal Count")
plt.ylabel("Number of Medals")
plt.xticks(rotation=45)
plt.show()
