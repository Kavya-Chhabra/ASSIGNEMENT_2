#n this task, you will identify lines that are nearly identical after basic normalization.
#Two lines are considered near-duplicates if they become identical after converting to lower-case
# and removing all whitespace and punctuation characters.
#Using sample-file.txt:
#• Identify sets of near-duplicate lines.
# • Print the number of such sets.
#• Print the first two sets you find, including line numbers and original lines

import string
from os import WCONTINUED

# Open the file and read all lines
file = open("sample-file.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

#Dictionary to group lines
# key = normalized line
# value = list of (line_number, original_line)
groups= {}

#Go through each line in the file
for i in range (len(lines)):
    original_line = lines[i].strip()

    #Build the normalized version of the line
    normalized = ""

    for char in original_line:

    #skip spaces and tabs
        if char.isspace():
            continue

    #skip punctuation
        if char in string.punctuation:
            continue

    #add lowercase version of the character
        normalized += char.lower()

    #ignore empty lines
    if normalized == "":
        continue

    # group lines with the same normalized version
    if normalized in groups:
        groups[normalized].append( (i + 1,original_line))
    else:
        groups[normalized] = [(i + 1, original_line)]

#creating a list for storing only near-duplicate sets
duplicate_sets = []

# Keep only groups that contain more than one line
for key in groups:
    if len(groups[key]) > 1:
        duplicate_sets.append(groups[key])

#print the number of near-duplicate sets
print("Number of near-duplicate sets:", len(duplicate_sets))

# print the first two sets
max_sets_to_print = 2
if len(duplicate_sets) < 2:
    max_sets_to_print = len(duplicate_sets)

#now we print hte first two near-duplicate sets
for s in range (max_sets_to_print):
    print("\nSet", s+1)

    #Each set contains line numbers and the original lines
    for line_number, text in duplicate_sets [s]:

        # Print the line number and original line text
        print(str(line_number) + ":", text)



