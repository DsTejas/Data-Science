import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load retail data
df = pd.read_csv("retail_data.csv", encoding='latin1')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Drop missing
df.dropna(inplace=True)

# Monetary = Total spent per customer
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Create RFM Table
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'count',
    'TotalPrice': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']
print(" RFM Table Preview:\n", rfm.head())

# Visualizations
sns.histplot(rfm['Recency'], bins=30, kde=True)
plt.title(" Recency Distribution")
plt.show()

sns.histplot(rfm['Frequency'], bins=30, kde=True)
plt.title(" Frequency Distribution")
plt.show()

sns.histplot(rfm['Monetary'], bins=30, kde=True)
plt.title(" Monetary Value Distribution")
plt.show()
