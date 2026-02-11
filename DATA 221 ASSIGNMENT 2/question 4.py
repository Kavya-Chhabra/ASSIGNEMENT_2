#Question 4:This question involves filtering tabular data and saving the results to a new file.
#Using student.csv:
#• Load the dataset into a DataFrame.
#• Filter students where study time ≥ 3, internet = 1, and absences ≤ 5.
#• Save the filtered data to high_engagement.csv.
#• Print the number of students saved and their average grade.

#import libraries
import pandas as pd

#first we have to load the student.csv file into the DataFrame
student_data = pd.read_csv("student.csv")

#Filter the students based on the given conditions:
#studytime >=3
#internet == 1 (has internet access)
# absences <= 5
high_engagement_students = student_data[
    (student_data["studytime"] >= 3) &
    (student_data["internet"] >= 1) &
    (student_data["absences"] >= 5)
]

# Save the filtered files to a new CSV file
high_engagement_students.to_csv("high_engagement.csv", index=False)

#Print how many students were saved
num_students = len(high_engagement_students)
print("Number of students saved:", num_students)

#calculate and print the average grade of these students
average_grade = high_engagement_students["grade"].mean()

#makes readability better if I round to 2 decimal places
print("Average grade:", round(average_grade,2))
