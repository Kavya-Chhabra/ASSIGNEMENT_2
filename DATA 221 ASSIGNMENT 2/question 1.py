#QUESTION 1:In this question, you will practice reading a text file and performing basic text preprocessing
#before computing word statistics.
#Using sample-file.txt:
#• Read the file and split it into tokens (words).
#• Convert all tokens to lowercase.
#• Remove punctuation characters from the beginning and end of each token.
#• Keep only tokens that contain at least two alphabetic characters.
#• Count word frequencies and print the 10 most frequent words in descending order in the
#format: word -> count.

import string

#first we must open the file in read mode and read everything inside of it
text_file = open("sample-file.txt", "r", encoding="utf-8")

#read the file contents into one long string
full_text_contents = text_file.read()

#make sure to always close the file, learned from CPSC 217
text_file.close()

#now we split the text into tokens using spaces, each token will be approximately one "word"
raw_word_tokens = full_text_contents.split()

#This list will store cleaned words that we must keep
cleaned_word_list = []

#now we clean the tokens one by one
for token in raw_word_tokens:
    #must convert the words into lower case so that all the words are consistently matching
    cleaned_token = token.lower()

    #now remove the punctuation(commas,)
    cleaned_token = token.strip(string.punctuation)

    #count the number of letters in the token
    alphabetic_letter_count = 0
    for character in cleaned_token:
        if character.isalpha():
            alphabetic_letter_count += 1
    #make sure to only keep the word if it has at least 2 letters
    if alphabetic_letter_count >= 2:
        cleaned_word_list.append(token)

#make a dictionary to count word frequencies
word_frequency_dictionary = {}

for word in cleaned_word_list:
    if word in word_frequency_dictionary:
        word_frequency_dictionary[word] += 1
    else:
        word_frequency_dictionary[word] = 1

#Convert dictionary to a list of (word,count) pairs
word_count_pairs = list(word_frequency_dictionary.items())

#sort by count from highest to lowest
word_count_pairs.sort(key=lambda x: x[1], reverse=True)

#print the top 10 most frequent words
for word_occurring_most_frequently in range (10):
    most_common_word = word_count_pairs[word_occurring_most_frequently][0]
    word_occurrence_count = word_count_pairs[word_occurring_most_frequently][1]
    print(most_common_word, "->", word_occurrence_count )

