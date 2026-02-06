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
file = open("sample-file.txt", "r", encoding="utf-8")

#read the file contents into one long string
text = file.read()

#make sure to always close the file, learned from CPSC 217
file.close()

#now we split the text into tokens using spaces, each token will be approximately one "word"
tokens = text.split()

#This list will store cleaned words that we must keep
words = []

#now we clean the tokens one by one
for token in tokens:
    #must convert the words into lower case so that all the words are consistently matching
    token = token.lower()

    #now remove the punctuation(commas,)
    token = token.strip(string.punctuation)

    #count the number of letters in the token
    letter_count = 0
    for char in token:
        if char.isalpha():
            letter_count += 1
    #make sure to only keep the word if it has at least 2 letters
    if letter_count >= 2:
        words.append(token)

#make a dictionary to count word frequencies
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#Convert dictionary to a list of (word,count) pairs
word_list = list(word_counts.items())

#sort by count from highest to lowest
word_list.sort(key=lambda x: x[1], reverse=True)

#print the top 10 most frequent words
for word_occurring_most_frequently in range (10):
    word = word_list[word_occurring_most_frequently][0]
    count = word_list[word_occurring_most_frequently][1]
    print(word, "->", count)

