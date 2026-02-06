#Question 9 (1 Point)
#In this question, you will extract tabular data from a webpage and store it in a structured format.
#Scrape the Wikipedia page:
#https://en.wikipedia.org/wiki/Machine_learning
#• Locate the first table inside the main content area (div with id mw-content-text) that
#contains at least 3 data rows.
#• Extract the table header from <th> tags if present; otherwise create headers named col1,
#col2, col3, etc.
#• Some rows may have fewer columns than others; pad missing values with empty strings.
#• Save the extracted table to wiki_table.csv.

import requests
from bs4 import BeautifulSoup
import csv

# Store Wikipedia URL in a variable
url = "https://en.wikipedia.org/wiki/Machine_learning"

#Adding a user agent so that wikipedia allows the request
headers = {"User-Agent": "Mozilla/5.0"}

#Downloading the webpage
response = requests.get(url, headers=headers)

#Now we will use Beautiful Soup to parse the HTML from the page
soup = BeautifulSoup(response.text, "html.parser")

#now we must find the paragraph inside the main article
main_content = soup.find("div",{"id":"mw-content-text"})

#Find all the tables inside the main content
tables = main_content.find_all("table")

#this will store the first valid table we find
chosen_table = None

#find the first table that has at least 3 data rows(rows with <td> cells)
for table in tables:
    rows = table.find_all("tr")

    data_row_count = 0
    max_columns = 0


    for row in rows:
        data_cells = row.find_all("td")

        if len(data_cells) > 0:
            data_row_count += 1

            #counting columns properly
            columns_in_this_row = 0
            for cell in data_cells:
                span_of_column = cell.get("span_of_column", 1)
                columns_in_this_row += int(span_of_column)

            # track the largest number of columns in any row
            if len(data_cells) > max_columns:
                max_columns = len(data_cells)

    #We want at least 3 data rows
    if data_row_count >= 3 and max_columns >=3:
        chosen_table = table
        break

#If a valid table is not found then stop the program
if chosen_table is None:
    print("No table with atleast 3 data rows was found")
else:
    #extract all rows from chosen table
    table_rows = chosen_table.find_all("tr")

    #We'll store the table as a list of lists(rows of text)
    extracted_rows = []

    #Go through each row and collect cell text from th/td
    for row in table_rows:
        cells = row.find_all(["th", "td"])

        #convert each cell to clean text
        row_values = []
        for cell in cells:
            cell_text = cell.get_text(separator= " ", strip=True)
            row_values.append(cell_text)

        #keep only non-empty rows
        if len (row_values) >0:
            extracted_rows.append(row_values)
    #Decide headers, if the first extracted row contains <th> values, treat it as the header row
    first_row_cells = table_rows[0].find_all(["th", "td"])
    first_row_has_th = (len(table_rows[0].find_all("th")) > 0)

    if first_row_has_th:
        headers_row = extracted_rows[0]
        data_rows = extracted_rows[1:]
    else:
        #if no headers are present we create default headers
        #But first find the maximum number of columns in the table
     max_columns = 0
    for r in extracted_rows:
        if len(r) > max_columns:
            max_columns = len(r)

    headers_row = []
    for i in range (1, max_columns + 1):
       headers_row.append("col" + str(i))

    data_rows = extracted_rows

#pad the rows so that they all have the same number of columns as the header
number_of_columns = len (headers_row)

padded_data_rows = []
for r in data_rows:
    #make a copy of the new row
    new_row = r[:]

    # If the row is too long, cut it down
    if len(new_row) > number_of_columns:
        new_row = new_row[:number_of_columns]

    padded_data_rows.append(new_row)

#save the table to wiki_table.csv
output_filename = "wiki_table.csv"
output_file = open(output_filename, "w", newline="", encoding="utf-8")

#create csv writer
writer = csv.writer(output_file)

#Write the header row first
writer.writerow(headers_row)

#Write the data rows
for r in padded_data_rows:
    writer.writerow(r)

#close the file
output_file.close()

#printing results
print("Saved table to", output_filename)
print("Columns:", len(headers_row))
print("Rows saved:", len(padded_data_rows))






