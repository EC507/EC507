import numpy as np
import pandas as pd

np.random.seed(98)
n = 250  # number of students

# Generate features
gpa = np.round(np.random.normal(3.0, 0.5, n), 2)
majors = np.random.choice(['CS', 'Math', 'Economics', 'History'], n)
clubs = np.random.poisson(2, n)
attendance = np.random.uniform(50, 100, n)

# Dropout logic: low GPA & low attendance
dropout_prob = (gpa < 2.5) & (attendance < 75)
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

# # Map dropout status to colors
# colors = df['Dropout'].map({0: 'blue', 1: 'pink'})

# # Scatter plot
# plt.figure(figsize=(7,10))
# plt.scatter(df['GPA'], df['Attendance'], c=colors, alpha=0.6)
# plt.xlabel("GPA")
# plt.ylabel("Attendance (%)")
# plt.title("Student Dropout Risk")
# plt.show()
print(df.describe())
print("\nDropout counts:")
print(df['Dropout'].value_counts())
# Mean stats for each group
print(df.groupby('Dropout')[['GPA', 'Attendance', 'Clubs']].mean())
print(df[df['Dropout'] == 1]['Major'].value_counts())
