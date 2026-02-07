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
crime_dataframe = pd.read_csv("crime.csv")

#create a new column called "risk"
# If ViolentCrimesPerPop >= 0.50 then HighCrime
#otherwise LowCrime

crime_risk_category_list = []

#Go through each violent crime value in the dataset
for violent_crime_rate in crime_dataframe["ViolentCrimesPerPop"]:
    if violent_crime_rate >= 0.50:
        crime_risk_category_list.append("HighCrime")
    else:
        crime_risk_category_list.append("LowCrime")

#Add the risk categories as a new column in the DataFrame
crime_dataframe["risk"] = crime_risk_category_list

#group the data by the risk column
#this seperates the dataset into HighCrime and LowCrime groups
crime_groups_by_risk = crime_dataframe.groupby("risk")

#Calaculate the average unemployment rate for each group by using the column percent_of_unemployed_people
average_unemployment_rates = crime_groups_by_risk ["PctUnemployed"].mean()

#print the results in a clear format
print("Average Unemployment rate by Crime Risk Level:\n")

#Loop through each risk category in the results (HighCrime and LowCrime)
for risk_level in average_unemployment_rates.index:

    #get the average unemployment value for the current risk group
    average_rate = average_unemployment_rates[risk_level]

    #printing the risk group and the average unemployment rate
    print(risk_level, "-> Average percent of unemployed people = ",round( average_rate, 2))
