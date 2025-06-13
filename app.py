
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Students_data.csv")

st.title("🎓 Student Performance Dashboard")

# Show the dataset
st.subheader("Student Records")
st.dataframe(df)

# Summary statistics
st.subheader("Average Marks by Course")
summary = df.groupby("Course")["Marks"].agg(["mean", "count"]).reset_index()
summary.columns = ["Course", "Average Marks", "Student Count"]
st.dataframe(summary)

# Bar chart for average marks
st.subheader("📊 Average Marks per Course")
fig, ax = plt.subplots()
ax.bar(summary["Course"], summary["Average Marks"], color="skyblue")
plt.xticks(rotation=15)
st.pyplot(fig)

# Pie chart for student distribution
st.subheader("👥 Student Distribution by Course")
fig2, ax2 = plt.subplots()
ax2.pie(summary["Student Count"], labels=summary["Course"], autopct="%1.1f%%", startangle=90)
ax2.axis("equal")
st.pyplot(fig2)

st.caption("Built with Streamlit | Data by Karumanchi Hemanth")
