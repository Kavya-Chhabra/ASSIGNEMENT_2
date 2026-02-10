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
machine_learning_wikipedia_url = "https://en.wikipedia.org/wiki/Machine_learning"

#Adding a user agent so that wikipedia allows the request
browser_request_headers = {"User-Agent": "Mozilla/5.0"}

#Downloading the webpage
wikipedia_page_response = requests.get(machine_learning_wikipedia_url, headers=browser_request_headers)

#Now we will use Beautiful Soup to parse the HTML from the page
parsed_wikipedia_html = BeautifulSoup(wikipedia_page_response .text, "html.parser")

#now we must find the paragraph inside the main article
main_article_content= parsed_wikipedia_html.find("div",{"id":"mw-content-text"})

#Find all the tables inside the main content
all_tables_in_main_content = main_article_content.find_all("table")

chosen_table = None
for table in all_tables_in_main_content:
    row_tags = table.find_all("tr")

    data_row_count = 0
    for row in row_tags:
        if row.find_all("td"):
            data_row_count += 1

    if data_row_count >= 3:
        chosen_table = table
        break

if chosen_table is None:
    print("No table with at least 3 data rows was found.")
    quit()

#extract rows from the chosen table (not from the whole page)
table_row_tags = chosen_table.find_all("tr")

# extract the table headers from <th> tags if they exist
table_headers = []
header_cells = table_row_tags[0].find_all("th")

if header_cells:
    for header_cell in header_cells:
        table_headers.append(header_cell.get_text(strip=True))
else:
    # If no headers exist, create default column names
    number_of_columns = len(table_row_tags[0].find_all("td"))
    table_headers = ["col" + str(column_index + 1) for column_index in range(number_of_columns)]

# Extract the table data rows
table_data_rows = []

for row_tag in table_row_tags[1:]:
    data_cells = row_tag.find_all(["th","td"])

    # Skip rows that contain no data
    if len(data_cells) == 0:
        continue

    # convert each cell into cleaned text
    extracted_row_values = []
    for cell in data_cells:
        extracted_row_values.append(cell.get_text("", strip=True))

    # Pad missing values with empty strings if needed
    while len(extracted_row_values) < len(table_headers):
        extracted_row_values.append("")

    table_data_rows.append(extracted_row_values)

# Save the extracted table into a CSV file
output_csv_filename = "wiki_table.csv"

with open(output_csv_filename, "w", newline="", encoding="utf-8") as output_file:
    csv_writer = csv.writer(output_file)

    # Write the header row first
    csv_writer.writerow(table_headers)

    # Write the table data rows
    csv_writer.writerows(table_data_rows)

#print for clarity and good habit
print("Saved table to", output_csv_filename)