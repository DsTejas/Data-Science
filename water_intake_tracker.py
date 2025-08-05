import pandas as pd
import matplotlib.pyplot as plt

# Recommended intake = 2.5 liters/day (can vary per person)
recommended_intake = 2.5  

# Water intake data (liters)
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Water_Intake_L': [1.8, 2.0, 2.6, 2.3, 3.0, 1.9, 2.7]
}

df = pd.DataFrame(data)

# Check how many days met or missed the goal
df['Met_Goal'] = df['Water_Intake_L'] >= recommended_intake

print("\n Weekly Water Intake Log:\n")
print(df)

# Summary
met_goal_days = df['Met_Goal'].sum()
missed_goal_days = len(df) - met_goal_days
avg_intake = df['Water_Intake_L'].mean()

print(f"\n Average Daily Intake: {avg_intake:.2f} L")
print(f" Days Met Hydration Goal: {met_goal_days}")
print(f" Days Missed Goal: {missed_goal_days}")

# Visualization
colors = ['green' if val else 'red' for val in df['Met_Goal']]

plt.figure(figsize=(10, 5))
plt.bar(df['Day'], df['Water_Intake_L'], color=colors)
plt.axhline(y=recommended_intake, color='blue', linestyle='--', label='Recommended Intake')
plt.title(" Daily Water Intake Analysis")
plt.xlabel("Day")
plt.ylabel("Liters")
plt.legend()
plt.tight_layout()
plt.show()
