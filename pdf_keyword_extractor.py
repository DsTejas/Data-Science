import PyPDF2
import re
from collections import Counter

# Load PDF
with open("sample.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()

# Preprocess text
words = re.findall(r'\b[a-zA-Z]{3,}\b', full_text.lower())

# Optional: filter out basic stopwords
stopwords = set([
    "the", "and", "for", "are", "that", "this", "with",
    "was", "from", "you", "have", "your", "not", "but", "can"
])
filtered_words = [word for word in words if word not in stopwords]

# Word frequency
word_count = Counter(filtered_words)

print(" Top 10 Keywords in PDF:")
for word, freq in word_count.most_common(10):
    print(f"{word}: {freq} times")

print(f"\n Total words: {len(words)}")
print(f"Unique words (after filtering): {len(set(filtered_words))}")
