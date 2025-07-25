import re
from collections import Counter

# Load SRT file
with open("sample_subtitle.srt", "r", encoding="utf-8") as f:
    content = f.read()

# Remove timestamps and line numbers
cleaned = re.sub(r'\d+\n', '', content)
cleaned = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> .*?\n', '', cleaned)

# Remove symbols and make lowercase
text_only = re.sub(r'[^\w\s]', '', cleaned).lower()

# Tokenize and remove short words
words = [word for word in text_only.split() if len(word) > 2]

# Optional: simple stopwords
stopwords = set([
    "the", "and", "you", "are", "that", "was", "for", "but", "not", "all", "she", "her", "him", "his"
])
filtered = [w for w in words if w not in stopwords]

# Frequency
freq = Counter(filtered)

print(" Top 15 Spoken Words in Subtitle File:")
for word, count in freq.most_common(15):
    print(f"{word}: {count} times")

print(f"\n Total Words: {len(words)}")
print(f" Unique (Filtered): {len(set(filtered))}")
