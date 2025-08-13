import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_name = "car_prices.csv"  # Change to your dataset file
try:
    df = pd.read_csv(file_name)
    print(f"File '{file_name}' loaded successfully!")
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found. Please place it in this folder.")
    exit()

# 1. Basic Info
print("\nShape of Data:", df.shape)
print("\nFirst 5 Rows:\n", df.head())
print("\nData Info:\n")
print(df.info())
print("\nSummary Statistics:\n", df.describe(include="all"))

# 2. Missing Values
print("\nMissing Values:\n", df.isnull().sum())

# 3. Remove Duplicates
duplicates = df.duplicated().sum()
if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print(f"\nRemoved {duplicates} duplicate rows.")

# 4. Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], kde=True, color="skyblue")
plt.title("Car Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

# 5. Price vs Year
if 'year' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='year', y='price', data=df)
    plt.title("Car Price by Year")
    plt.xticks(rotation=45)
    plt.show()

# 6. Price by Brand
if 'brand' in df.columns:
    brand_avg = df.groupby('brand')['price'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=brand_avg.index, y=brand_avg.values, palette="viridis")
    plt.title("Average Car Price by Brand")
    plt.xticks(rotation=45)
    plt.ylabel("Average Price")
    plt.show()

# 7. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 8. Price vs Mileage
if 'mileage' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='mileage', y='price', data=df, alpha=0.6)
    plt.title("Car Price vs Mileage")
    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.show()

print("\nAnalysis Complete!")
