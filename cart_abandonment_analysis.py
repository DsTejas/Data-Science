import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cart_abandonment_data.csv")

# Preview data
print("🛍 Sample data:\n", df.head())

# Cart abandonment rate by device
sns.barplot(x='device_type', y='cart_abandoned', data=df, estimator=lambda x: sum(x)/len(x), palette='coolwarm')
plt.title(" Cart Abandonment Rate by Device")
plt.ylabel("Abandonment Rate")
plt.xlabel("Device Type")
plt.show()

# Time of day vs abandonment
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
sns.boxplot(x='hour', y='cart_abandoned', data=df)
plt.title(" Cart Abandonment by Hour of Day")
plt.ylabel("Abandoned (0 = No, 1 = Yes)")
plt.show()

# Average session duration comparison
sns.boxplot(x='cart_abandoned', y='session_duration', data=df, palette='Set2')
plt.title(" Session Duration vs Cart Abandonment")
plt.xticks([0, 1], ["Completed", "Abandoned"])
plt.show()
