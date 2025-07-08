import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("credit_card_data.csv")

# Show basic info
print(" Columns:\n", df.columns)
print(" Preview:\n", df.head())

# Distribution of purchase amounts
plt.figure(figsize=(8, 5))
sns.histplot(df['Purchase Amount'], bins=30, color='skyblue')
plt.title(" Distribution of Purchase Amount")
plt.xlabel("Amount")
plt.show()

# Avg purchase by gender
sns.barplot(data=df, x='Gender', y='Purchase Amount', estimator=lambda x: x.mean(), palette='Set2')
plt.title(" Average Purchase by Gender")
plt.show()

# Spending by age group
df['Age Group'] = pd.cut(df['Age'], bins=[18, 25, 35, 50, 65], labels=['18–25', '26–35', '36–50', '51–65'])
sns.boxplot(data=df, x='Age Group', y='Purchase Amount', palette='cool')
plt.title("Purchase Amount by Age Group")
plt.show()
