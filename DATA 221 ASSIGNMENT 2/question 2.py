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
input_text_file = open("sample-file.txt", "r", encoding="utf-8")

#now read the file
full_text_contents = input_text_file.read()

#good coding practice to always close a file
input_text_file.close()

#next we must split the text into seperate tokens
raw_word_tokens = full_text_contents.split()

#make a list to store all of the "clean" words
cleaned_word_list = []

#individually clean and filter each token
for raw_token in raw_word_tokens:
    cleaned_token = raw_token.lower()

    #make sure to remove punctuation
    cleaned_token = cleaned_token.strip(string.punctuation)

    #count how many letters are in each token
    alphabetic_character_count= 0
    for character in cleaned_token:
        if character.isalpha():
            alphabetic_character_count += 1
    #only words wit more than 2 letters will be kept

    if alphabetic_character_count >= 2:
        cleaned_word_list.append(cleaned_token)

# a bigram is two consecutive words and we will create a list to store all of them
bigram_list = []

#scan through the word list and create pairs
for index in range(len(cleaned_word_list)- 1):
    bigram = cleaned_word_list[index] + " " + cleaned_word_list[index + 1]
    bigram_list.append(bigram)

# now we must convert the dictionary into a list of (bigram,count) pairs
bigram_counts = {}

#count the number of times each bigram appears
for bigram in bigram_list:
    if bigram in bigram_counts:
        bigram_counts[bigram] +=1
    else:
        bigram_counts[bigram] = 1

#now we sort the bigrams in highest to lowest frequency
sorted_bigram = list(bigram_counts.items())

#sort bigrams by frequency from highest to lowest
sorted_bigram.sort(key=lambda x: x[1], reverse=True)

#Print the top 5 most frequent bigrams
number_of_bigrams_to_print = 5

if len(sorted_bigram) < 5:
    number_of_bigrams_to_print = len(sorted_bigram)

#looping through the number of bigrams we decided to print
for rank in range (number_of_bigrams_to_print):

    #getting the words from the list(bigrams)
    bigram = sorted_bigram[rank][0]

    #counting how many times it appears
    count = sorted_bigram[rank][1]

    #printing
    print(bigram, "->", count)


