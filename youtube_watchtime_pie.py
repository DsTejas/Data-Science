import pandas as pd
import matplotlib.pyplot as plt

# Sample watch time data (in minutes)
data = {
    'Category': ['Education', 'Music', 'Entertainment', 'News', 'Gaming'],
    'WatchTime': [240, 180, 300, 90, 150]
}

df = pd.DataFrame(data)

# Print the table
print("\n🕒 YouTube Watch Time Breakdown:\n")
print(df)

# Pie chart visualization
plt.figure(figsize=(8, 8))
plt.pie(df['WatchTime'], labels=df['Category'], autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#99ff99','#ff9999','#ffcc99','#c2c2f0'])
plt.title(" YouTube Watch Time by Category")
plt.axis('equal')  # Ensures pie chart is circular
plt.tight_layout()
plt.show()
