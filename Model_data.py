#import spacy
import csv
import pandas as pd
from Word_tokenizer import *
import random
from spacy.training.example import Example
import spacy

resume_keys = [
    "Objective",
    "Summary",
    "Computer",
    "Data",
    "Profile",
    "Professional Summary",
    "Career Summary",
    "Qualifications",
    "Skills",
    "python",
    "january",
    "August",
    "industry",
    "yechnical",
    "exprience"
    "Areas of Expertise",
    "Key Skills",
    "Technical Skills",
    "Education",
    "Academic Background",
    "Professional Experience",
    "Work Experience",
    "javascript",
    "Employment History",
    "Relevant Experience",
    "Projects",
    "Certifications",
    "Awards and Honors",
    "Achievements",
    "Publications",
    "Languages",
    "Interests",
    "Volunteer Work",
    "References",
]


resume_keys = get_most_used_words('UpdatedResumeDataSet.csv')

resume_keys = resume_keys[:150]
#print(resume_keys)

resume_first_val = [check[0] for check in resume_keys]

df = pd.read_csv('UpdatedResumeDataSet.csv')
dataset = df['Resume']
#print(dataset.iloc[0])


#dataset = dataset.str.lower()

# data of all the most common resume words
# to check the keyword percentage, take every single value per resume, then how many of the mosst common words would be in 
# resume, divide it by the total lengeth of the original commonw ords dataset. 

def calculate_keyword_percentage(df, resume_keywords):
    
    percentage_array = []
    for index, row in df.iterrows():
        total_sum = len(resume_keywords)
        total_amt = 0
        words = row['Resume'].split()
        my_set = set()
        for word in words:
            if word in resume_keywords and word not in my_set:
                total_amt+=1
                my_set.add(word)
        #print(total_amt)
        #print(total_sum)
        percentage_array.append((float)(total_amt / total_sum) * 100)
        #print(percentage_array[0])
        #break
    
    return percentage_array


def calculate_single_percentage(words, resume_keywords):
    total_sum = len(resume_keywords)
    total_amt = 0
    #words = row['Resume'].split()
    my_set = set()
    for word in words:
        if word in resume_keywords and word not in my_set:
            total_amt+=1
            my_set.add(word)
    return (float)(total_amt / total_sum) * 100

##################


df_part_one = df.head(len(df)//2)
df_part_two = df.tail(len(df)//2)

percentage_array = calculate_keyword_percentage(df, resume_first_val)
#print(percentage_array)



def returnGoodBadResumes(percentage_array):

    index = 0
    good_resumes = []
    bad_resumes = []
    for percent in percentage_array:
        # get data only from the column required
        #required = resume['Resume']
        #print(percent)
        if percent >= 25:
            good_resumes.append(dataset[index])
        else: bad_resumes.append(dataset[index])
        index +=1

    #print("Length good:", len(good_resumes))
    #print("Length bad:",len(bad_resumes))

    return good_resumes, bad_resumes


# #check the database and do NLP:
#nlp = spacy.load('en_core_web_sm')


def addColumnGoodBad(percentage_array):
    vals = []
    for percent in percentage_array:
        if percent >= 25:
            vals.append("Good")
        else: vals.append("Bad")
    df["Good or Bad"] = vals
addColumnGoodBad(percentage_array)
#This method is through Chat GPT

#this method taken from the internet and chat gpt
def train_spacy() :
    addColumnGoodBad(percentage_array)
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    new_df = df.iloc[:, -2:]

    # Define the training configurations
    config = {
        'epochs': 10,
        'batch_size': 8,
        'learning_rate': 0.001,
    }

    # # Create training data in spaCy format
    train_data = []
    for text, label in zip(df['Resume'], df['Good or Bad']):
        # Convert label to binary (1 for good, 0 for bad)
        label_binary = 1 if label == 'good' else 0
        train_data.append((text, {'cats': {'Good': label_binary, 'Bad': 1 - label_binary}}))

    # # Initialize the text classification pipeline in spaCy
    text_cat = nlp.add_pipe('textcat', config={'exclusive_classes': True, 'architecture': 'simple_cnn'})
    text_cat.add_label('Good')
    text_cat.add_label('Bad')

    # # Train the model
    random.shuffle(train_data)
    for epoch in range(config['epochs']):
        losses = {}
        for text, annotations in train_data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.5, losses=losses)
        print(f'Epoch {epoch + 1}, Loss: {losses["textcat"]:.3f}')

    # # Save the trained model to a file
    nlp.to_disk('Spacyload.txt')


def assess_resume(resume_text):
    # train_spacy()
    # nlp = spacy.load('Spacyload.txt')
    nlp = spacy.load('en_core_web_sm')
    resume_analysis = nlp(resume_text)
    #print(resume_analysis)
    words = [token.text for token in resume_analysis]
    percent = calculate_single_percentage(words, resume_first_val)
    
    #print(percent)
    if percent >= 25:
        return ("Good resume", percent)
    else : return ("Bad resume", percent)


def getMissingWords(resume_text, used_words):
    vals = []
    for word in resume_text:
        if word not in used_words:
            vals.append(word)

    return vals

