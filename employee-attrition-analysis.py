import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_attrition.csv")

# Basic overview
print("👥 Data preview:\n", df[['Age', 'JobRole', 'Attrition', 'MonthlyIncome']].head())

# Attrition count
sns.countplot(x='Attrition', data=df, palette='pastel')
plt.title("🚪 Employee Attrition Count")
plt.show()

# Age distribution by attrition
sns.histplot(data=df, x='Age', hue='Attrition', multiple='stack', bins=30)
plt.title("📊 Age vs Attrition")
plt.show()

# Monthly income by job role
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='JobRole', y='MonthlyIncome', hue='Attrition')
plt.title("💸 Income Distribution by Job Role and Attrition")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
