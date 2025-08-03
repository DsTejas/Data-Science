import pandas as pd
import matplotlib.pyplot as plt

# Simulated screen time data in hours
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Screen_Time_Hours': [3.5, 4, 6, 5.5, 7, 8.5, 4.5]
}

df = pd.DataFrame(data)

# Show table
print("\n Weekly Screen Time (in hours):\n")
print(df)

# Visualize with both line and bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['Day'], df['Screen_Time_Hours'], color='lightcoral', label='Bar')
plt.plot(df['Day'], df['Screen_Time_Hours'], color='blue', marker='o', label='Line')

plt.axhline(y=6, color='green', linestyle='--', label='Healthy Limit (6 hrs)')
plt.title(" Daily Screen Time Tracker")
plt.xlabel("Day")
plt.ylabel("Screen Time (Hours)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the chart
plt.show()
