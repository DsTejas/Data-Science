import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset with missing values
file_path = "data_with_missing.csv"
df = pd.read_csv(file_path)

# Display basic null value counts
print("\n🔍 Missing Value Summary:\n")
print(df.isnull().sum())

# Plot missing value heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="YlGnBu", yticklabels=False)
plt.title("Heatmap of Missing Values in Dataset")
plt.tight_layout()
plt.show()
