
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load IPL match dataset
df = pd.read_csv("ipl_matches.csv")

# Preview data
print(df.head())

# Top teams with most wins
top_winners = df['winner'].value_counts().head(10)

plt.figure(figsize=(9, 5))
sns.barplot(x=top_winners.values, y=top_winners.index, palette='viridis')
plt.title("🏆 Top 10 IPL Teams by Wins")
plt.xlabel("Number of Wins")
plt.ylabel("Teams")
plt.tight_layout()
plt.show()

# Toss decision analysis
plt.figure(figsize=(6, 4))
sns.countplot(x='toss_decision', data=df, palette='pastel')
plt.title("🎲 Toss Decision Distribution")
plt.tight_layout()
plt.show()

# Toss winner and match winner relation
same_toss_match = df[df['toss_winner'] == df['winner']]
count_same = same_toss_match.shape[0]
total = df.shape[0]

print(f"\nTeams that won both toss and match: {count_same} out of {total} matches")

# Matches played at top venues
top_venues = df['venue'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_venues.values, y=top_venues.index, palette='coolwarm')
plt.title("🏟️ Top 10 Venues by Number of Matches")
plt.xlabel("Matches Played")
plt.ylabel("Venue")
plt.tight_layout()
plt.show()

# Matches over the years
df['year'] = pd.to_datetime(df['date']).dt.year
matches_per_year = df['year'].value_counts().sort_index()

plt.figure(figsize=(8, 4))
sns.lineplot(x=matches_per_year.index, y=matches_per_year.values, marker='o')
plt.title("📈 Matches Played Per Year in IPL")
plt.xlabel("Year")
plt.ylabel("Number of Matches")
plt.tight_layout()
plt.show()
