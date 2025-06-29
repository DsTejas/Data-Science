# house_price_prediction.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset (example: California housing or Kaggle dataset)
df = pd.read_csv("housing.csv")

# Show basic info
print("📄 Data preview:")
print(df.head())

# Drop nulls if any
df.dropna(inplace=True)

# Select features and target
X = df[['MedInc', 'AveRooms', 'AveOccup', 'HouseAge']]  # feature example
y = df['MedHouseVal']  # target: median house value

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

print("✅ R² Score:", r2_score(y_test, y_pred))
print("📉 RMSE:", mean_squared_error(y_test, y_pred, squared=False))

# Plot actual vs predicted
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('🏠 Actual vs Predicted House Prices')
plt.grid(True)
plt.show()
