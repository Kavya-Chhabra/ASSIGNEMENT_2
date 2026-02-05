#Question 6:Question 6 (1 Point)
#In this question, you will create a simple category based on crime levels and compare unem-
#ployment rates between the groups.
#Using crime.csv:
#• Load the dataset into a pandas DataFrame.
#• Create a new column called risk based on ViolentCrimesPerPop:
#– If ViolentCrimesPerPop is greater than or equal to 0.50, set risk = "High-
#Crime".
#– Otherwise, set risk = "LowCrime".
#• Group the data by the risk column.
#• For each group, calculate the average value of PctUnemployed.
#• Print the average unemployment rate for both HighCrime and LowCrime groups in a
#clear format

import pandas as pd

#Load the crime.csv dataset into DataFrame
crime_data = pd.read_csv("crime.csv")

#create a new column called "risk"
# If ViolentCrimesPerPop >= 0.50 then HighCrime
#otherwise LowCrime

risk_categories = []

#Go through each violent crime value in the dataset
for crime_value in crime_data["ViolentCrimesPerPop"]:
    if crime_value >= 0.50:
        risk_categories.append("HighCrime")
    else:
        risk_categories.append("LowCrime")

#Add the risk categories as a new column in the DataFrame
crime_data["risk"] = risk_categories

#group the data by the risk column
#this seperates the dataset into HighCrime and LowCrime groups
grouped_by_risk = crime_data.groupby("risk")

#Calaculate the average unemployment rate for each group by using the column percent_of_unemployed_people
average_unemployment_rates = grouped_by_risk ["PctUnemployed"].mean()

#print the results in a clear format
print("Average Unemployment rate by Crime Risk Level:\n")

#Loop through each risk category in the results (HighCrime and LowCrime)
for risk_level in average_unemployment_rates.index:

    #get the average unemployment value for the current risk group
    average_rate = average_unemployment_rates[risk_level]

    #printing the risk group and the average unemployment rate
    print(risk_level, "-> Average percent of unemployed people = ",round( average_rate, 2))
