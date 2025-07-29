import matplotlib.pyplot as plt
from collections import Counter
import string

# Load and read the text file
with open("sample_text.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

# Remove punctuation and split into words
translator = str.maketrans("", "", string.punctuation)
words = text.translate(translator).split()

# Count word frequencies
word_counts = Counter(words)

# Show top 10 most common words
top_words = word_counts.most_common(10)
print(" Top 10 Words:")
for word, count in top_words:
    print(f"{word}: {count}")

# Plot the top 10 words
words, counts = zip(*top_words)
plt.figure(figsize=(10, 5))
plt.bar(words, counts, color='skyblue')
plt.title("Top 10 Word Frequencies")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
