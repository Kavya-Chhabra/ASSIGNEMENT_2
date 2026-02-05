#question 5:Here you will create a new categorical variable and generate a grouped summary table.
#Using student.csv:
#• Create a new column grade_band:
#– Low: grade ≤ 9
#– Medium: grade 10–14
#– High: grade ≥ 15
#• Create a grouped summary table showing for each band:
#– number of students
#– average absences
#– percentage of students with internet access
#• Save the table as student_bands.csv

import pandas as pd

# first we have to load the data from the student.csv
student_data = pd.read_csv("student.csv")

#create a new column based on the final grade that includes
#low: grade<=9
#medium: grade 10 to 14
#high: grade>= 15
grade_bands = []

for grade in student_data["grade"]:
    if grade <=9:
        grade_bands.append("Low")
    elif grade<= 14:
        grade_bands.append("Medium")
    else:
        grade_bands.append("High")

#add the new list as a column in the DataFrame
student_data["grade_band"] = grade_bands

#Group the data by grade_band and calculate the required values
#1) number of students
#2) average absences
#3) percentage with internet access

summary_table = student_data.groupby("grade_band").agg(
    number_of_students = ("grade","count"),
    average_absences = ("absences", "mean"),
    percent_of_students_with_internet=("internet", "mean")
)

#percent_of_students_with_internet is currently a decimal (ex: 0.75), so convert to percentage (ex: 75.0)
summary_table["percent_of_students_with_internet"] = summary_table["percent_of_students_with_internet"] * 100

#save the summary table to student_bands.csv
summary_table.to_csv("student_bands.csv")

#rounding the values so that they are cleaner
summary_table = summary_table.round(2)

# Print the table
print(summary_table)
