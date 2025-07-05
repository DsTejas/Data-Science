import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('medical_data.csv')

# View first few rows
print(df.head())

# Dataset shape
print("Shape:", df.shape)

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Data types and non-null counts
print(df.info())

# Summary statistics
print(df.describe())

# Count of each gender
print(df['Gender'].value_counts())

# Count of heart disease cases
print(df['Heart_Disease'].value_counts())

# Plot gender distribution
sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.show()

# Plot heart disease distribution
sns.countplot(x='Heart_Disease', data=df)
plt.title('Heart Disease Count')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()

# Age distribution by heart disease
sns.histplot(data=df, x='Age', hue='Heart_Disease', multiple='stack')
plt.title('Age vs Heart Disease')
plt.show()

# Correlation matrix
corr = df.corr(numeric_only=True)
print("Correlation matrix:\n", corr)

# Correlation heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Convert Yes/No in Diabetes column to 1/0
df['Diabetes'] = df['Diabetes'].replace({'Yes': 1, 'No': 0})

# Cholesterol vs Heart Disease
sns.boxplot(x='Heart_Disease', y='Cholesterol', data=df)
plt.title('Cholesterol vs Heart Disease')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()
