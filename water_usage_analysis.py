import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Water usage in liters per day
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Water_Usage_Liters': [120, 150, 135, 200, 180, 220, 160]
}

df = pd.DataFrame(data)

# Display data
print("\n Weekly Water Consumption:\n")
print(df)

# Summary statistics
total_water = df['Water_Usage_Liters'].sum()
avg_water = df['Water_Usage_Liters'].mean()
max_day = df.loc[df['Water_Usage_Liters'].idxmax()]
min_day = df.loc[df['Water_Usage_Liters'].idxmin()]

print(f"\n Total Weekly Water Usage: {total_water} liters")
print(f" Average Daily Usage: {avg_water:.2f} liters")
print(f" Highest Usage Day: {max_day['Day']} ({max_day['Water_Usage_Liters']} liters)")
print(f" Lowest Usage Day: {min_day['Day']} ({min_day['Water_Usage_Liters']} liters)")

# Visualization - Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df['Day'], df['Water_Usage_Liters'], color='blue', alpha=0.7)

plt.title(" Weekly Water Usage Pattern")
plt.xlabel("Day")
plt.ylabel("Water Usage (Liters)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt
