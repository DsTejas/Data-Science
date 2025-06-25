# 📌 Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 🔹 Load the 'tips' dataset - contains restaurant bills and tips info
tips = sns.load_dataset('tips')

# 🔍 Preview the dataset to understand it
print("Sample of Tips Dataset:\n", tips.head())

# 🎯 1. Scatter Plot: Total Bill vs Tip
# Helps understand if people who spend more also tip more
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')
plt.title('Total Bill vs Tip by Gender')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()

# 🎯 2. Histogram + KDE: Distribution of Total Bill
# Useful to understand customer spending behavior
sns.histplot(data=tips, x='total_bill', kde=True, color='skyblue')
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Count')
plt.show()

# 🎯 3. Bar Plot: Average Tip by Day
# Shows which day people tip the most on average
avg_tip_by_day = tips.groupby('day')['tip'].mean().reset_index()
sns.barplot(data=avg_tip_by_day, x='day', y='tip', palette='Set2')
plt.title('Average Tip by Day')
plt.ylabel('Average Tip ($)')
plt.show()

# 🎯 4. Box Plot: Tip % Comparison between Genders
# Helps to compare tipping behavior between males and females
tips['tip_percent'] = (tips['tip'] / tips['total_bill']) * 100
sns.boxplot(data=tips, x='sex', y='tip_percent', palette='coolwarm')
plt.title('Tip Percentage by Gender')
plt.ylabel('Tip %')
plt.show()

# 🎯 5. Heatmap: Correlation between Numeric Features
# Managers can see which metrics are closely related
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='Blues')
plt.title('Correlation Heatmap')
plt.show()

# 🎯 6. Count Plot: Number of Customers (Lunch vs Dinner)
# Tells us which time slot is busier
sns.countplot(data=tips, x='time', palette='pastel')
plt.title('Customer Count by Time of Day')
plt.ylabel('Number of Customers')
plt.show()

# 🎯 7. Pairplot: All numeric variables with respect to Gender
# Great for exploring relationships between multiple variables
sns.pairplot(tips, hue='sex', palette='husl')
plt.suptitle('Pairwise Relationships in Tips Dataset', y=1.02)
plt.show()
