import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("job_salary_data.csv")

# Encode categorical columns
label_cols = ['title', 'location', 'experience_level', 'industry']
for col in label_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

# Features and target
X = df.drop('salary', axis=1)
y = df['salary']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(" R² Score:", r2_score(y_test, y_pred))
print(" MAE:", mean_absolute_error(y_test, y_pred))

# Visualization
sns.scatterplot(x=y_test, y=y_pred)
plt.title(" Actual vs Predicted Salaries")
plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.grid(True)
plt.show()
