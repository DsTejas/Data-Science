import numpy as np
import matplotlib.pyplot as plt

# Simulated 30-day temperature data in Celsius
np.random.seed(1)
temperature_data = np.random.normal(loc=32, scale=5, size=30).round(1)  # mean=32°C, std=5°C

# Stats
max_temp = np.max(temperature_data)
min_temp = np.min(temperature_data)
avg_temp = np.mean(temperature_data)

print("Temperature Stats for the Month")
print(f" Max Temperature: {max_temp}°C")
print(f" Min Temperature: {min_temp}°C")
print(f" Average Temperature: {avg_temp:.2f}°C")

# Heatwave: days over 37°C
heatwave_days = np.where(temperature_data > 37)[0] + 1

# Cold spell: days below 25°C
cold_days = np.where(temperature_data < 25)[0] + 1

print(f"\n Heatwave Days ( > 37°C): {heatwave_days.tolist()}")
print(f" Cold Days ( < 25°C): {cold_days.tolist()}")

# Plot temperature trend
plt.plot(range(1, 31), temperature_data, marker='o', color='orange')
plt.axhline(37, color='red', linestyle='--', label='Heatwave Threshold (37°C)')
plt.axhline(25, color='blue', linestyle='--', label='Cold Threshold (25°C)')
plt.title("Daily Temperature Trend")
plt.xlabel("Day of Month")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.show()
