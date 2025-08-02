import pandas as pd
import matplotlib.pyplot as plt

# Simulated sleep data (in hours)
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Sleep_Hours': [6.5, 7, 5.5, 6, 8, 9, 7.5]
}

df = pd.DataFrame(data)

# Display table
print("\n Weekly Sleep Duration (in hours):\n")
print(df)

# Visualizing with a bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Day'], df['Sleep_Hours'], color='skyblue')

# Highlight bars below recommended sleep (7 hrs)
for bar in bars:
    if bar.get_height() < 7:
        bar.set_color('red')

plt.axhline(y=7, color='green', linestyle='--', label='Recommended Sleep (7 hrs)')
plt.title(" Sleep Duration Throughout the Week")
plt.xlabel("Day")
plt.ylabel("Hours Slept")
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Show chart
plt.show()
