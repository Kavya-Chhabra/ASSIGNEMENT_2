# DATA 221 Assignment 2

This repository contains my solutions for Assignment 2 in DATA 221.

Each question is written in its own Python file (question 1.py to question 10.py).  
The assignment focuses on text processing, working with CSV datasets, and basic web scraping using BeautifulSoup.

---

## Question Breakdown

- **Question 1 (question 1.py)**  
  Reads sample-file.txt, cleans the words (lowercase + punctuation removal), filters out short tokens, and prints the 10 most frequent words.

- **Question 2 (question 2.py)**  
  Uses the cleaned word list from the same text file to build bigrams (pairs of consecutive words), counts them, and prints the 5 most common bigrams.

- **Question 3 (question 3.py)**  
  Finds near-duplicate lines in the text file by removing punctuation/whitespace and comparing normalized versions of each line.

- **Question 4 (question 4.py)**  
  Loads student.csv, filters students with high study time, internet access, and low absences, then saves the result to high_engagement.csv and prints summary stats.

- **Question 5 (question 5.py)**  
  Adds a grade band column (Low/Medium/High) to the student dataset, groups by band, calculates averages and percentages, and saves the output to student_bands.csv.

- **Question 6 (question 6.py)**  
  Uses crime.csv to classify communities into HighCrime or LowCrime based on violent crime rate, then compares average unemployment between the two groups.

- **Question 7 (question 7.py)**  
  Scrapes the Wikipedia page for Data Science and prints the page title along with the first main paragraph.

- **Question 8 (question 8.py)**  
  Extracts all main <h2> section headings from the Data Science Wikipedia page excluding reference sections and saves them to headings.txt.

- **Question 9 (question 9.py)**  
  Scrapes the Machine Learning Wikipedia page, finds the first table with at least 3 data rows, extracts the contents, and saves it as wiki_table.csv.

- **Question 10 (question 10.py)**  
  Implements a function that searches through a file and returns all line numbers and text where a keyword appears (case-insensitive).

## Output Files Included

- high_engagement.csv  
- student_bands.csv 
- headings.txt 
- wiki_table.csv
