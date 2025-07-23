from PIL import Image
import matplotlib.pyplot as plt
from collections import Counter

# Load image
img = Image.open("sample.jpg")
img = img.resize((150, 150))  # Resize for faster processing

# Convert to RGB
pixels = list(img.getdata())

# Count most frequent color
most_common = Counter(pixels).most_common(1)[0]
dominant_color = most_common[0]
pixel_count = most_common[1]

print(f" Dominant Color (RGB): {dominant_color}")
print(f" Occurrence: {pixel_count} pixels")

# Visualize
plt.figure(figsize=(4, 4))
plt.imshow([[dominant_color]])
plt.title("Dominant Color")
plt.axis("off")
plt.tight_layout()
plt.show()
