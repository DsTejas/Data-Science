import pandas as pd
import matplotlib.pyplot as plt

# Sample reading log data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Pages_Read': [30, 45, 25, 50, 60, 90, 40],
    'Genre': ['Fiction', 'Fiction', 'Non-Fiction', 'Fiction', 'Fantasy', 'Fantasy', 'Non-Fiction']
}

df = pd.DataFrame(data)

# Display raw data
print("\n Weekly Book Reading Log:\n")
print(df)

# Summary
total_pages = df['Pages_Read'].sum()
avg_pages = df['Pages_Read'].mean()
most_read_genre = df['Genre'].value_counts().idxmax()

print(f"\n Total Pages Read: {total_pages}")
print(f" Average Daily Pages: {avg_pages:.2f}")
print(f" Most Frequent Genre: {most_read_genre}")

# Visualization - Genre distribution
genre_counts = df['Genre'].value_counts()

plt.figure(figsize=(7, 5))
genre_counts.plot(kind='bar', color='purple')
plt.title("Genre Distribution for the Week")
plt.xlabel("Genre")
plt.ylabel("Number of Days Read")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
