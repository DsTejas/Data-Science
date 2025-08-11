import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load the file (put ur dataset name here)
df = pd.read_csv("your_dataset.csv")

# shape of data (rows, cols) just to know how big it is
print("Shape:", df.shape)

# look first few rows just to get idea
print("\nFirst 5 rows:\n", df.head())

# info abt each column (type, null etc.)
print("\nData Info:")
print(df.info())

# some stats, mean, std, min max etc. for numeric and obj cols also
print("\nSummary Stats:\n", df.describe(include='all'))

# check null values, so we know what to clean
print("\nMissing Values:\n", df.isnull().sum())

# check duplicates (maybe some rows repeated by mistake)
print("\nDuplicate Rows:", df.duplicated().sum())

# see type of each col
print("\nData Types:\n", df.dtypes)

# how many unique vals in each col
print("\nUnique Values Count:\n", df.nunique())

# plot heatmap for correlations (only numbers)
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")  # colorful chart to see relationships
plt.show()

# plot histograms for numeric cols
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols].hist(bins=20, figsize=(12, 8), color="skyblue", edgecolor="black")
plt.suptitle("Numeric Columns Distribution")  # helps see spread
plt.show()

# countplots for each category col
cat_cols = df.select_dtypes(exclude=np.number).columns
for col in cat_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(x=col, data=df, palette="Set2")
    plt.title(f"Count Plot - {col}")  # see freq of each category
    plt.xticks(rotation=45)
    plt.show()

# boxplots to check outliers in numeric data
for col in num_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df[col], color="lightgreen")
    plt.title(f"Boxplot - {col}")  # outliers are the dots away from box
    plt.show()
