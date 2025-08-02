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
