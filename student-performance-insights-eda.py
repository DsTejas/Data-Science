import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Make charts cleaner
sns.set(style="whitegrid")

# Load dataset (sample)
data = {
    'gender': ['female', 'male', 'female', 'male', 'female', 'male', 'female', 'female', 'male', 'male'],
    'parent_edu': ['bachelor', 'some college', 'high school', 'associate', 'master', 'high school', 'some college', 'bachelor', 'associate', 'bachelor'],
    'test_prep': ['completed', 'none', 'completed', 'none', 'completed', 'none', 'none', 'completed', 'none', 'completed'],
    'math_score': [72, 69, 90, 47, 76, 58, 64, 77, 53, 67],
    'reading_score': [72, 90, 95, 57, 78, 52, 60, 86, 44, 76],
    'writing_score': [74, 88, 93, 44, 75, 50, 57, 83, 42, 73]
}
df = pd.DataFrame(data)

# Show sample rows
print("🎓 Sample Student Data:")
print(df.head())

# 🔍 Look at average scores by gender
print("\n📊 Average Scores by Gender:")
print(df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean())

# 📈 Visualize score distributions
sns.histplot(df['math_score'], kde=True, color='lightblue')
plt.title("📐 Math Score Distribution")
plt.show()

# 📘 Reading score based on test preparation
sns.boxplot(x='test_prep', y='reading_score', data=df)
plt.title("📘 Reading Scores vs Test Preparation")
plt.show()

# 📚 Writing score comparison across parental education levels
sns.barplot(x='parent_edu', y='writing_score', data=df)
plt.title("🖋️ Writing Score by Parental Education")
plt.xticks(rotation=45)
plt.show()

# 🔗 Correlation heatmap
sns.heatmap(df[['math_score', 'reading_score', 'writing_score']].corr(), annot=True, cmap='viridis')
plt.title("📊 Score Correlations")
plt.show()

# 📌 Insights
print("\n📌 Insights:")
print("- Female students tend to score slightly higher.")
print("- Students who completed test preparation scored better.")
print("- Parental education level may influence student performance.")
