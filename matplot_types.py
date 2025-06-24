import matplotlib.pyplot as plt
import numpy as np

# 1. Basic Line Plot
x = [1, 2, 3, 4, 5]           # X-axis values
y = [2, 3, 5, 7, 11]         # Y-axis values (prime numbers)
plt.figure(figsize=(6,4))    # Set figure size (width x height in inches)
plt.plot(x, y, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6)
plt.title('Basic Line Plot')
plt.xlabel('X Values')       # Label for X-axis
plt.ylabel('Prime Numbers')  # Label for Y-axis
plt.grid(True)               # Add grid lines
plt.show()

# 2. Bar Plot
labels = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
plt.bar(labels, values, color='green')
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 3. Horizontal Bar Plot
plt.barh(labels, values, color='orange')
plt.title('Horizontal Bar Plot')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.show()

# 4. Scatter Plot
x = np.random.rand(50)
y = np.random.rand(50)
sizes = 100 * np.random.rand(50)  # Size of each point
colors = np.random.rand(50)       # Color based on intensity
plt.scatter(x, y, s=sizes, c=colors, alpha=0.7, cmap='viridis')
plt.title('Scatter Plot with Random Data')
plt.colorbar(label='Intensity')
plt.show()

# 5. Pie Chart
sizes = [15, 30, 45, 10]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
explode = (0, 0.1, 0, 0)   # "Explode" the second slice (Bananas)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Fruit Distribution Pie Chart')
plt.axis('equal')          # Equal aspect ratio ensures that pie is a circle.
plt.show()

# 6. Histogram
np.random.seed(42)
data = np.random.randn(1000)  # Generate 1000 random numbers from normal distribution
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 7. Multiple Lines on One Plot
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)', color='blue')
plt.plot(x, np.cos(x), label='cos(x)', color='red')
plt.title('Sine and Cosine Functions')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()               # Show legend
plt.grid(True)
plt.show()


