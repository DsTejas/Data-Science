import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("youtube_channel_data.csv")

# Preview
print(df.head())

# Most viewed videos
top_views = df[['Title', 'Views']].sort_values(by='Views', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='Views', y='Title', data=top_views, palette='magma')
plt.title(" Top 10 Most Viewed Videos")
plt.xlabel("Views")
plt.ylabel("Video Title")
plt.tight_layout()
plt.show()

# Likes vs Dislikes scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Likes', y='Dislikes', data=df, color='teal')
plt.title("Likes vs  Dislikes")
plt.xlabel("Likes")
plt.ylabel("Dislikes")
plt.grid(True)
plt.tight_layout()
plt.show()

# Comments distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Comment Count'], bins=30, kde=True, color='blue')
plt.title(" Comment Count Distribution")
plt.xlabel("Number of Comments")
plt.tight_layout()
plt.show()

# Views by category
category_views = df.groupby("Category")['Views'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=category_views.index, y=category_views.values, palette='cool')
plt.title(" Total Views by Video Category")
plt.xlabel("Category")
plt.ylabel("Total Views")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
