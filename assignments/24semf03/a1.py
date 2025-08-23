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
dropout_prob = (gpa < 2.5) & (attendance < 70)
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
