# 📌 Step 1: Import required libraries
import pandas as pd

# 📌 Step 2: Sample web log dataset with inconsistent values
data = {
    'user_id': [101, 102, 103, 104, 105, 105],
    'login_time': ['2025-06-01 10:00', '2025/06/01 10:05', None, '01-06-2025 10:10', '2025-06-01T10:15', '2025-06-01T10:15'],
    'location': ['Mumbai', 'DELHI', 'mumbai', 'Bangalore', 'DELHI', 'DELHI']
}
df = pd.DataFrame(data)

# 📌 Step 3: Display raw log data
print("Raw User Log Data:")
print(df)

# ✅ Step 4: Remove duplicate log entries
df = df.drop_duplicates()

# ✅ Step 5: Standardize date formats
df['login_time'] = pd.to_datetime(df['login_time'], errors='coerce')

# ✅ Step 6: Standardize location names (capitalize first letter only)
df['location'] = df['location'].str.capitalize()

# 📌 Step 7: Final cleaned log data
print("\nCleaned User Log Data:")
print(df)
