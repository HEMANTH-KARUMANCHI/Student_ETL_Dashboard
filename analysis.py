import pandas as pd
import matplotlib.pyplot as plt


# Load the CSV file into a DataFrame
csv_path="C:\\Users\\Hemanth\\Documents\\Projects_2025\\Student_Management_System\\Students_data.csv"
data=pd.read_csv(csv_path)

#Transform

#clean course names
data['Course']=data['Course'].str.title().str.strip()

# Calculate average marks per course
avg_marks = data.groupby('Course')['Marks'].mean().reset_index(name='Average Marks')

# Count students per course
student_counts = data['Course'].value_counts().reset_index()
student_counts.columns = ['Course', 'Student Count']

# Merge both summaries
summary = pd.merge(avg_marks, student_counts, on='Course')

# Step 3: Load - Save the summary to a new CSV
summary_path = "C:\\Users\\Hemanth\\Documents\\Projects_2025\\Student_Management_System\\Summary.csv"
summary.to_csv(summary_path, index=False)

summary_path

