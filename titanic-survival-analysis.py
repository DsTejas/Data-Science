import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv('titanic.csv')

# Basic info
print("🧾 Dataset shape:", df.shape)
print(df.head())

# Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Drop irrelevant columns
df.drop(['Cabin', 'Name', 'Ticket'], axis=1, inplace=True)

# Convert categorical features to numeric
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Split data
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Classification Report:\n", classification_report(y_test, y_pred))

# Visualization: Survival by class and gender
sns.barplot(x='Pclass', y='Survived', hue='Sex_male', data=df)
plt.title('🎯 Survival Rate by Class and Gender')
plt.ylabel('Survival Probability')
plt.show()
