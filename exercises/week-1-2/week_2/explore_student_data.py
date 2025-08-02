import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

# Summary statistics
print(df.describe())

# Dropout counts
print(df['Dropout'].value_counts())

# Average GPA by major
print(df.groupby('Major')['GPA'].mean())

# Filter high-risk students
high_risk = df[(df['GPA'] < 2.5) & (df['Attendance'] < 70)]
print(high_risk.head())
