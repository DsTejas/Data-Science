# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Step 2: Load the dataset
df = pd.read_csv('bank.csv')  # Replace with the correct path if needed

# Step 3: Preview the data
print("First 5 rows of the dataset:")
print(df.head())

# Step 4: General information about the dataset
print("\nDataset Info:")
print(df.info())

# Step 5: Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())

# Step 6: Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 7: Explore categorical columns
print("\nCategorical column breakdown:")
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nUnique value counts for '{col}':")
    print(df[col].value_counts())

# Step 8: Distribution of the target variable
sns.countplot(x='y', data=df, palette='Set2')
plt.title('Target Variable Distribution - Term Deposit Subscription')
plt.xlabel('Subscribed')
plt.ylabel('Count')
plt.show()

# Step 9: Age distribution
sns.histplot(df['age'], bins=30, kde=True, color='skyblue')
plt.title('Age Distribution of Clients')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Step 10: Job vs subscription
sns.countplot(y='job', hue='y', data=df, palette='Set3')
plt.title('Term Deposit Subscription by Job Type')
plt.xlabel('Count')
plt.ylabel('Job')
plt.legend(title='Subscribed')
plt.show()

# Step 11: Marital status vs subscription
sns.countplot(x='marital', hue='y', data=df, palette='Set1')
plt.title('Subscription by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.legend(title='Subscribed')
plt.show()

# Step 12: Education vs subscription (if column exists)
if 'education' in df.columns:
    sns.countplot(x='education', hue='y', data=df, palette='Set2')
    plt.title('Subscription by Education Level')
    plt.xlabel('Education')
    plt.ylabel('Count')
    plt.legend(title='Subscribed')
    plt.xticks(rotation=45)
    plt.show()

# Step 13: Balance vs subscription
sns.boxplot(data=df, x='y', y='balance', palette='coolwarm')
plt.title('Account Balance by Subscription Status')
plt.xlabel('Subscribed')
plt.ylabel('Balance')
plt.show()

# Step 14: Contact type vs subscription (if column exists)
if 'contact' in df.columns:
    sns.countplot(x='contact', hue='y', data=df, palette='Set1')
    plt.title('Subscription by Contact Type')
    plt.xlabel('Contact Type')
    plt.ylabel('Count')
    plt.legend(title='Subscribed')
    plt.show()

# Step 15: Month-wise subscription trend (if column exists)
if 'month' in df.columns:
    month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                   'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    sns.countplot(x='month', hue='y', data=df, palette='Set3', order=month_order)
    plt.title('Subscription by Month')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.legend(title='Subscribed')
    plt.show()
