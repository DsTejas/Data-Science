import csv
from collections import Counter
import matplotlib.pyplot as plt

# Load CSV file
file_path = "people_names.csv"  # Make sure this file exists

first_names = []
last_names = []

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if present
    for row in reader:
        if len(row) >= 1:
            full_name = row[0].strip().title()  # e.g. "Tejas"
            parts = full_name.split()
            if len(parts) >= 2:
                first_names.append(parts[0])
                last_names.append(parts[1])

# Count frequencies
first_name_counts = Counter(first_names)
last_name_counts = Counter(last_names)

# Most common names
print("Most Common First Names:")
for name, count in first_name_counts.most_common(5):
    print(f"{name}: {count} times")

print("\n Most Common Last Names:")
for name, count in last_name_counts.most_common(5):
    print(f"{name}: {count} times")

# Plot
top_first = first_name_counts.most_common(10)
names, counts = zip(*top_first)

plt.figure(figsize=(10, 5))
plt.bar(names, counts, color="purple")
plt.title("Top 10 Most Common First Names")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
