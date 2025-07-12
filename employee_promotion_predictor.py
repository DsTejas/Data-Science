import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("employee_promotion.csv")

# Encode categorical columns
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# Define X and y
X = df.drop('is_promoted', axis=1)
y = df['is_promoted']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print(" Accuracy:", accuracy_score(y_test, y_pred))
print(" Report:\n", classification_report(y_test, y_pred))

# Visual: Promotions by Department
sns.countplot(data=df, x='department', hue='is_promoted', palette='Set2')
plt.title(" Promotions by Department")
plt.xticks(rotation=45)
plt.show()
