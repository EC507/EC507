import numpy as np
import pandas as pd

np.random.seed(42)
n = 200  # number of students

# Generate features
gpa = np.round(np.random.normal(3.0, 0.5, n), 2)
majors = np.random.choice(['CS', 'Math', 'Economics', 'History'], n)
clubs = np.random.poisson(2, n)
attendance = np.random.uniform(50, 100, n)

# Dropout logic: low GPA & low attendance
dropout_prob = (gpa < 3.5) & (attendance < 70)
dropout = np.where(dropout_prob, 1, 0)

# Create DataFrame
df = pd.DataFrame({
    'GPA': gpa,
    'Major': majors,
    'Clubs': clubs,
    'Attendance': np.round(attendance, 1),
    'Dropout': dropout
})

print(df.head())

# Save to CSV for later use
df.to_csv("students.csv", index=False)
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Map dropout status to colors
colors = df['Dropout'].map({0: 'green', 1: 'red'})

# Scatter plot
plt.figure(figsize=(6,4))
plt.scatter(df['GPA'], df['Attendance'], c=colors, alpha=0.6)
plt.xlabel("GPA")
plt.ylabel("Attendance (%)")
plt.title("Student Dropout Risk")
plt.show()
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
high_risk = df[(df['GPA'] < 3.5) & (df['Attendance'] < 70)]
print(high_risk.head())
print(((gpa < 3.5) & (attendance < 70)).sum())
