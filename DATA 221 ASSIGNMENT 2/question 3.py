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
input_file = open("sample-file.txt", "r", encoding="utf-8")
all_lines_in_the_file = input_file.readlines()
input_file.close()

#Dictionary to group lines
# key = normalized line
# value = list of (line_number, original_line)
normalized_line_groups= {}

#Go through each line in the file
for line_index in range (len(all_lines_in_the_file)):
    original_line_text = all_lines_in_the_file[line_index].strip()

    #Build the normalized version of the line
    normalized_line_text = ""

    for character in original_line_text:

    #skip spaces and tabs
        if character.isspace():
            continue

    #skip punctuation
        if character in string.punctuation:
            continue

    #add lowercase version of the character
        normalized_line_text += character.lower()

    #ignore empty lines
    if normalized_line_text == "":
        continue

    # group lines with the same normalized version
    if normalized_line_text in normalized_line_groups:
        normalized_line_groups[normalized_line_text].append( (line_index + 1,original_line_text))
    else:
        normalized_line_groups[normalized_line_text] = [(line_index + 1, original_line_text)]

#creating a list for storing only near-duplicate sets
duplicate_sets = []

# Keep only groups that contain more than one line
for normalized_key in normalized_line_groups:
    if len(normalized_line_groups[normalized_key]) > 1:
        duplicate_sets.append(normalized_line_groups[normalized_key])

#print the number of near-duplicate sets
print("Number of near-duplicate sets:", len(duplicate_sets))

# print the first two sets
maximum_sets_to_print = 2
if len(duplicate_sets) < 2:
    maximum_sets_to_print = len(duplicate_sets)

#now we print hte first two near-duplicate sets
for set_index in range (maximum_sets_to_print):
    print("\nSet", set_index+1)

    #Each set contains line numbers and the original lines
    for line_number, text in duplicate_sets [set_index]:

        # Print the line number and original line text
        print(str(line_number) + ":", text)



