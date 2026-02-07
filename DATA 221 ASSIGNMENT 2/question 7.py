#question 7:n this question, you will work on extracting structured content from a webpage using Beautiful-Soup.
#Scrape the Wikipedia page:
#https://en.wikipedia.org/wiki/Data_science
#Write a program using requests and BeautifulSoup that:
#• Extracts and prints the page title from the <title> tag.
#• Extracts the first paragraph from the main article content inside the div with id mw-
#content-text.
#• The paragraph must contain at least 50 characters (after stripping whitespace)

#requests is the library used to download the HTML content of a webpage
import requests

#BeautifulSoup is the library that we use to extract information from HTML
from bs4 import BeautifulSoup


#We have to store the URL in a variable
wikipedia_page_url = "https://en.wikipedia.org/wiki/Data_science"

#this is needed so that Wikipedia treats this request like a real browser
request_headers = {"User-Agent":"Mozilla/5.0"}

#sending a request and downloading the page HTML
page_response = requests.get(wikipedia_page_url, headers=request_headers)


#Now we will use Beautiful Soup to parse the HTML from the page
parsed_html_page = BeautifulSoup(page_response.text, "html.parser")

#Extract and print the page title
title_of_the_page = parsed_html_page.find("title").get_text()
print("The title of the page is:", title_of_the_page)

#now we must find the paragraph inside the main article
main_content = parsed_html_page.find("div",{"id":"mw-content-text"})

#all the paragraphs will contain all <p> tags under main_content
paragraph_tag_list = main_content.find_all("p")

# now we go through each paragraph and find the first one that had 50 or more characters
for paragraph in paragraph_tag_list:
    paragraph_text = paragraph.get_text().strip()

    #check the length after stripping the whitespace
    if len(paragraph_text) >= 50:

        #printing the label
        print("\nFirst paragraph:")

        #printing the actual paragraph
        print(paragraph_text)

        #after the first valid paragraph is printed we stop
        break
