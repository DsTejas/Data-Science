import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load IPL dataset
df = pd.read_csv("ipl_2023_batting.csv")

# Preview
print(df.head())

# Total runs by each player
top_scorers = df.groupby("Player")["Runs"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
top_scorers.plot(kind='bar', color='crimson')
plt.title("🏏 Top 10 Run Scorers - IPL 2023")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Strike Rate per Player
df['Strike Rate'] = (df['Runs'] / df['Balls Faced']) * 100

top_strikers = df.groupby("Player")['Strike Rate'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
top_strikers.plot(kind='bar', color='limegreen')
plt.title("Top 10 Strike Rates - IPL 2023")
plt.ylabel("Strike Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Team-wise total runs
team_runs = df.groupby("Team")["Runs"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
team_runs.plot(kind='bar', color='navy')
plt.title(" Total Team Runs - IPL 2023")
plt.ylabel("Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
