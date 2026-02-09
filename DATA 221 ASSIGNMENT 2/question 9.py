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

#filter out navigation/layout tables
filtered_candidate_tables= []
for table_tag in all_tables_in_main_content:
    table_class_list = table_tag.get("class") or []

    #skip if it's a layout table
    if "navbox" in table_class_list or "vertical-navbox" in table_class_list or "metadata" in table_class_list:
        continue

    #otherwise keep it as a candidate
    filtered_candidate_tables.append(table_tag)

#find the first variable with at least 3 data rows (data row = a row with <td> cells)
# A data row contains actual <td> cells which proves it has actual table data
chosen_valid_table = None


for table_tag in filtered_candidate_tables:
    #all rows in this table
    table_row_tags = table_tag.find_all("tr")

    number_of_data_rows = 0
    maximum_data_columns_seen = 0

    # go through the rows and count haw many have data cells
    for row_tag in table_row_tags:
        data_cell_tags = row_tag.find_all("td")

        #considered data row if it has at least on data cell
        if len(data_cell_tags) > 0:
            number_of_data_rows += 1

            #count the number of columns, track widest data row
            if len(data_cell_tags) > maximum_data_columns_seen:
                maximum_data_columns_seen = len(data_cell_tags)
        #must have at least 3 data rows

    #only decide if it's valid after checking the whole table, need at least 3 rows and 3 columns
    if number_of_data_rows >= 3 and maximum_data_columns_seen >= 3:
        chosen_valid_table = table_tag
        #stop at the first valid table
        break

#if valid table is not found then print and stop
if chosen_valid_table is None:
    print("No table with at least 3 data rows was found.")
else:
    #extract rows from the chosen table
    chosen_table_row_tags = chosen_valid_table.find_all("tr")

    #building a list of rows where each row is a list of cell strings
    extracted_table_rows_as_lists = []

    for row_tag in chosen_table_row_tags:

        #keep both th and td for detection of header row
        header_and_data_cells = row_tag.find_all(["th", "td"])

        #skip empty rows
        if len(header_and_data_cells) == 0:
            continue

        #convert the cells into cleaned text strings
        current_row_text_values = []
        for cell_tag in header_and_data_cells:
            #separator keeps text readable
            cleaned_cell_text = cell_tag.get_text(separator=" ", strip=True)
            current_row_text_values.append(cleaned_cell_text)


        extracted_table_rows_as_lists.append(current_row_text_values)

        # decide header row:
        #If the first extracted row has any <th>, treat it as headers. Otherwise create col1..colN.
    first_row_has_th = (len(chosen_table_row_tags[0].find_all("th")) > 0)

    if first_row_has_th and len(extracted_table_rows_as_lists[0]) > 1:
        table_header_row = extracted_table_rows_as_lists[0]
        table_data_rows = extracted_table_rows_as_lists[1:]
    else:
        #find maximum columns extracted rows so our default headers match the widest rows
        maximum_column_count = 0
        for row_list in extracted_table_rows_as_lists:
            if len(row_list) > maximum_column_count:
                maximum_column_count = len(row_list)

        table_header_row = []
        for column_number in range (1, maximum_column_count + 1):
            table_header_row.append("col" + str(column_number))

        table_data_rows = extracted_table_rows_as_lists

    #Pad the data rows so that every row has thw same number of columns as the header row
    total_number_of_columns = len(table_header_row)
    padded_table_data_rows = []

    for original_data_row in table_data_rows:
        padded_row = original_data_row[:] # we don't want to mess with the original row

        #if a row is too long then we trim it
        if len(padded_row) > total_number_of_columns:
            padded_row = padded_row[:total_number_of_columns]

        #if a row is too short then we have to pad it with empty strings
        while len(padded_row) < total_number_of_columns:
            padded_row.append("")

        padded_table_data_rows.append(padded_row)

    #write to csv file
    output_csv_filename = "wiki_table.csv"
    with open(output_csv_filename, "w", newline="", encoding="utf-8") as csv_output_file:
        csv_writer = csv.writer(csv_output_file)

        #write header first
        csv_writer.writerow(table_header_row)

        #write each padded row
        for padded_row in padded_table_data_rows:
            csv_writer.writerow(padded_row)

    #print confirmation
    print("Saved table to", output_csv_filename)
    print("columns:", len(table_header_row))
    print("rows saved:", len(padded_table_data_rows))

