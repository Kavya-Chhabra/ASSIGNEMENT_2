#Question 2:In this question, you will analyze pairs of consecutive words (called bigrams) from a text file.
#Using sample-file.txt:
#• Read the file and split it into tokens (words).
#• Convert all tokens to lowercase.
#• Remove punctuation characters from the beginning and end of each token.
#• Keep only tokens that contain at least two alphabetic characters.
#• Construct bigrams (pairs of consecutive cleaned words).
#• Count the frequency of each bigram.
#• Print the 5 most frequent bigrams in descending order in the format: word1 word2 ->count.

import string

#first we must open the file and read its contents
text_file = open("sample-file.txt", "r", encoding="utf-8")

#now read the file
file_contents = text_file.read()

#was done for debugging purposes to make sure code doesn't crash
print("Chars in file:", len(file_contents))

#good coding practice to always close a file
text_file.close()

#next we must split the text into seperate tokens
raw_tokens = file_contents.split()

#make a list to store all of the "clean" words
cleaned_words = []

#individually clean and filter each token
for token in raw_tokens:
    token = token.lower()

    #make sure to remove punctuation
    token = token.strip(string.punctuation)

    #count how many letters are in each token
    count_of_letters = 0
    for char in token:
        if char.isalpha():
            count_of_letters += 1
    #only words wit more than 2 letters will be kept

    if count_of_letters >= 2:
        cleaned_words.append(token)

# a bigram is two consecutive words and we will create a list to store all of them
bigrams = []

#scan through the word list and create pairs
for i in range(len(cleaned_words)- 1):
    bigram = cleaned_words[i] + " " + cleaned_words[i+1]
    bigrams.append(bigram)

# now we must convert the dictionary into a list of (bigram,count) pairs
bigram_counts = {}

#count the number of times each bigram appears
for bg in bigrams:
    if bg in bigram_counts:
        bigram_counts[bg] +=1
    else:
        bigram_counts[bg] = 1

#now we sort the bigrams in highest to lowest frequency
sorted_bigram = list(bigram_counts.items())

#sort bigrams by frequency from highest to lowest
sorted_bigram.sort(key=lambda x: x[1], reverse=True)

#Print the top 5 most frequent bigrams
number_of_bigrams_to_print = 5

if len(sorted_bigram) < 5:
    number_of_bigrams_to_print = len(sorted_bigram)

#looping through the number of bigrams we decided to print
for i in range (number_of_bigrams_to_print):

    #getting the words from the list(bigrams)
    bigram = sorted_bigram[i][0]

    #counting how many times it appears
    count = sorted_bigram[i][1]

    #printing
    print(bigram, "->", count)


