#Question 8
#This task focuses on extracting structured heading information from a webpage.
#Using the same Wikipedia page:
#https://en.wikipedia.org/wiki/Data_science
#• Extract all <h2> section headings from the main content area (div with id mw-content-
#text).
#• Do not include headings containing the words: References, External links, See also, or
#Notes.
#• Remove any [edit] text from headings.
#• Save the headings to headings.txt, one per line, in order


import requests
from bs4 import BeautifulSoup

# Store Wikipedia URL in a variable
wikipedia_page_url = "https://en.wikipedia.org/wiki/Data_science"

#Adding a user agent so that wikipedia allows the request
request_headers = {"User-Agent": "Mozilla/5.0"}

#Downloading the webpage
page_response = requests.get(wikipedia_page_url, headers=request_headers)

#Now we will use Beautiful Soup to parse the HTML from the page
parsed_html_page = BeautifulSoup(page_response.text, "html.parser")

#now we must find the paragraph inside the main article
main_article_content = parsed_html_page.find("div",{"id":"mw-content-text"})

#finding all the <h2> headings inside of the main content
h2_heading_tags = main_article_content.find_all("h2")

#write out which words we do not want to include in the headings
excluded_heading_words = ["References", "External links", "See also", "Notes"]

#make a list to store the cleaned headings
cleaned_heading_list = []

#Loop through each heading and clean it
for heading_tag in h2_heading_tags:

    #get the text of the heading and remove extra spaces
    heading_text = heading_tag.get_text().strip()

    #remove "[edit]" text if it appears
    heading_text = heading_text.replace("[edit]", "").strip()

    #check if the heading contains any excluded words
    skip_heading = False
    for word in excluded_heading_words:
        if word in heading_text:
            skip_heading = True

            #once we know that it should be skipped stop checking
            break

    # If the heading should not be skipped, save it
    if skip_heading == False and heading_text != "":
        cleaned_heading_list.append(heading_text)

#Save headings to headings.txt(one per line)
output_file = open("headings.txt","w", encoding="utf-8")

for heading in cleaned_heading_list:
    output_file.write(heading + "\n")

output_file.close()

#Print confirmation message
print("Saved", len(cleaned_heading_list), "headings to headings.txt")




