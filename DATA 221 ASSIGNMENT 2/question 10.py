#Question 10 (1 Point)
#This final question asks you to design a reusable function for searching within text files.
#Write a function:
#1)def find_lines_containing(filename, keyword):
#2) """
#3) Returns a list of (line_number, line_text) for lines that contain ←↩keyword
#4) (case-insensitive). Line numbers start at 1.
#5 """
#Test the function using sample-file.txt with keyword lorem.
#Assignment No 2 Page 5
#• Print how many matching lines were found.
#• Print the first 3 matching lines (line number and text).

def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines contain
    the keyword (case-insensitive). Line numbers start at 1.
    """

    #List to store matching lines
    matching_lines = []

    #Open the file and read line by line
    file = open(filename,"r", encoding="utf-8")

    line_number = 1

    for line in file:
        #remove extra newline spaces
        line_text = line.strip()

        #Check if keyword is in the line(case-insensitive)
        if keyword.lower() in line_text.lower():
            matching_lines.append((line_number, line_text))

        #Move to the next line number
        line_number +=1
    #close the file after reading
    file.close()

    return matching_lines

#Test using the sample-file.txt with keyword "lorem"
results = find_lines_containing("sample-file.txt", "lorem")

#Print how many matching lines were found
print("Number of matching lines", len(results))

#Print the first 3 matching lines
print("\nFirst 3 matching lines:")

#prevents errors if there are fewer than 3 matches
for i in range(min(3, len(results))):

    #Each result is a tuple: (line_number, line_text)
    line_num, text = results[i]

    #Print the line number and the original line text
    print(str(line_num) + ":", text)
