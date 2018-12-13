# File Name: main.py
# Date: 12-10-2018
# Author: Zhen Yang
# Purpose: Assess the passage for each of the following:
# - Approximate word count
# - Approximate sentence count
# - Approximate letter count (per word)
# - Average sentence length (in words)

# Module for creating file paths across operating systems
import os

# Module for regular expression
import re

# Error handling 
try:

    # Prompt for user to enter file name
    input_file = input("Please enter the file name in raw_data folder to analyze: ")

    # Open file
    with open(f"raw_data/{input_file}", 'r') as raw_file:
        paragraph = raw_file.read()

        # Split paragrash into words
        words = paragraph.split()
        
        # Split paragraph into sentences
        sentences = re.split("(?<=[.!?]) +", paragraph)

        # Word Count
        word_count = len(words)
     
        # Sentence Count
        sentence_count = len(sentences)
    
        # Average Letter Count
        average_letter_count = round(sum(len(word) for word in words) / word_count, 1)

        # Average Sentence Length
        average_sentence_length = round(sum(len(sentence.split()) for sentence in sentences) / sentence_count, 1)

        # Print result to terminal
        print("Paragraph Analysis ")
        print("------------------- ")
        print(f"Approximate Word Count: {word_count}")
        print(f"Approximate Sentence Count: {sentence_count}")
        print(f"Average Letter Count: {average_letter_count}")
        print(f"Average Sentence Length: {average_sentence_length}")

# Handle print or file error
except IOError as e:
   print("IO error: " + str(e))

# Handle other errors such as re error
except: 
   print("Unexpected error. Please check the data")