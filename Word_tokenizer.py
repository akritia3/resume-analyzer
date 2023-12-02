import csv
from collections import Counter
import re
import string
from collections import Counter
import nltk
import random
import csv
import pandas as pd


#chat gpt for this method.
def get_most_used_words(csv_file_path):
    # Open the CSV file and read it using the csv.reader
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        word_counter = Counter()

        # Iterate through rows and extract words from the "Resume" column
        for row in reader:
            resume_text = row.get("Resume", "")
            
            # Use regular expression to extract words (you may need to adjust this based on your specific requirements)
            words = re.findall(r'\b\w+\b', resume_text.lower())
            
            # Update the Counter with the words from the current row
            word_counter.update(words)

    # Get the most common words and their counts
    most_common_words = word_counter.most_common()

    return most_common_words


most_used_words = get_most_used_words('UpdatedResumeDataSet.csv')

word_necessary = []
for word, count in most_used_words[:200]:
    if(len(word) > 4) : 
        word_necessary.append(word)
        #print(f"{word}: {count}") 