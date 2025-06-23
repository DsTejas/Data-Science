#Employee analysis using pandas
import pandas as pd

def load_data(file_path):
    """Load employee data from CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully.")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def clean_data(df):
    """Clean missing values in the dataset."""
    df_cleaned = df.dropna(subset=['Department', 'Salary'])  # Drop rows with missing critical info
    df_cleaned['Salary'] = df_cleaned['Salary'].fillna(df['Salary'].mean())  # Fill missing salaries with mean
    print("🧹 Data cleaned.")
    return df_cleaned

def analyze_data(df):
    """Perform basic analysis on employee data."""
    print("\n📊 Basic Statistics:")
    print(df.describe())

    print("\n🔍 Average salary by department:")
    print(df.groupby('Department')['Salary'].mean().sort_values(ascending=False))

def filter_high_salary(df, threshold=80000):
    """Filter employees earning more than a threshold."""
    high_salary = df[df['Salary'] > threshold]
    print(f"\n💼 Employees with salary > {threshold}:")
    print(high_salary[['Name', 'Department', 'Salary']])
    return high_salary

def save_results(df, output_file):
    """Save filtered results to a new CSV."""
    df.to_csv(output_file, index=False)
    print(f"📁 Filtered data saved to {output_file}")

def main():
    file_path = 'employees.csv'  # Input CSV file
    output_file = 'high_salary_employees.csv'  # Output file

    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        analyze_data(df)
        high_salary_df = filter_high_salary(df, threshold=80000)
        save_results(high_salary_df, output_file)

if __name__ == "__main__":
    main()
