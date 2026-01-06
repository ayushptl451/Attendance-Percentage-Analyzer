import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = {
        "Student": ["ayush patel", "aarchi", "aayu", "aaru", "aarushi", "anshikha", "suhani", "ayush"],
        "Total_Classes": [100, 100, 100, 100, 100, 100, 100, 100],
        "Classes_Attended": [92, 75, 60, 45, 88, 70, 55, 30]
    }

    df = pd.DataFrame(data)

    # Avoid division by zero
    df["Attendance_Percentage"] = np.where(
        df["Total_Classes"] > 0,
        (df["Classes_Attended"] / df["Total_Classes"]) * 100,
        0
    )

    df["Attendance_Percentage"] = df["Attendance_Percentage"].round(2)

    conditions = [
        df["Attendance_Percentage"] >= 85,
        (df["Attendance_Percentage"] >= 60) & (df["Attendance_Percentage"] < 85),
        df["Attendance_Percentage"] < 60
    ]

    categories = ["Good", "Average", "Poor"]
    df["Category"] = np.select(conditions, categories, default='')

    print("\nAttendance Report:\n")
    print(df)

    df.to_csv("attendance_report.csv", index=False)
    print("\nReport saved as 'attendance_report.csv'")

    plt.figure(figsize=(8, 5))
    plt.bar(df["Student"], df["Attendance_Percentage"])
    plt.xlabel("Students")
    plt.ylabel("Attendance Percentage")
    plt.title("Student Attendance Percentage")
    plt.show()

    plt.figure(figsize=(6, 6))
    category_counts = df["Category"].value_counts()
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
    plt.title("Attendance Category Distribution")
    plt.show()

if __name__ == "__main__":
    main()