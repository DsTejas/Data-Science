import pandas as pd
import matplotlib.pyplot as plt

# Load bank transaction data
df = pd.read_csv("transactions.csv")

# Display sample
print(" Sample Transactions:")
print(df.head())

# Ensure 'Amount' is numeric
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Basic statistics
total_credit = df[df['Type'] == 'Credit']['Amount'].sum()
total_debit = df[df['Type'] == 'Debit']['Amount'].sum()

print(f"\n Total Credit: ₹{total_credit:.2f}")
print(f" Total Debit: ₹{total_debit:.2f}")

# Monthly expenses
df['Month'] = df['Date'].dt.to_period('M')
monthly_spending = df[df['Type'] == 'Debit'].groupby('Month')['Amount'].sum()

# Plot monthly spending
monthly_spending.plot(kind='bar', color='tomato')
plt.title(" Monthly Debit Amounts")
plt.xlabel("Month")
plt.ylabel("Amount Spent (₹)")
plt.tight_layout()
plt.show()

# Top 5 largest transactions
top_txns = df.sort_values(by='Amount', ascending=False).head(5)
print("\n Top 5 Transactions:")
print(top_txns[['Date', 'Description', 'Type', 'Amount']])

# Frequent expenses (if 'Category' exists)
if 'Category' in df.columns:
    top_categories = df[df['Type'] == 'Debit']['Category'].value_counts().head(5)
    print("\n Top 5 Spending Categories:")
    print(top_categories)
