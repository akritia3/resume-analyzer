
import csv
import pandas as pd

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
    "technical",
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

resume_keywords = [value.lower() for value in resume_keys]
# data_temp = []
# with open('/Users/vikrampidaparthi/Documents/CS222_Project/group-project-team69/UpdatedResumeDataSet 3.csv', 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         #data_temp = [row[1] for row in reader]
#         print(row)
#         break
# print(data_temp)
# dataset = []
# dataset.append(row[1] in data_temp[1])
#dataset = [row[1] for row in data_temp[1:]]



df = pd.read_csv('/Users/vikrampidaparthi/Documents/CS222_Project/group-project-team69/UpdatedResumeDataSet 3.csv')
dataset = df['Resume']
#print(dataset.iloc[0])


dataset = dataset.str.lower()






def calculate_keyword_percentage(df, resume_keywords):
    
    percentage_array = []
    for index, row in df.iterrows():
        total_sum = len(resume_keywords)
        total_amt = 0
        words = row['Resume'].split()
        
        for word in words:
            if word in resume_keywords:
                total_amt+=1
        print(total_amt)
        print(total_sum)
        percentage_array.append((float)(total_amt / total_sum) * 100)
        print(percentage_array[0])
        #break
    
    return percentage_array
    

percentage_array = calculate_keyword_percentage(df, resume_keywords)

index = 0
good_resumes = []
bad_resumes = []
for percent in percentage_array:
    # get data only from the column required
    #required = resume['Resume']
    #print(percent)
    if percent >= 30:
        good_resumes.append(dataset[index])
    else: bad_resumes.append(dataset[index])
    index +=1

print("Length good:", len(good_resumes))
print("Length bad:",len(bad_resumes))

#check the database and do NLP:

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Define your set of keywords and their importance scores
keywords = {
    "Objective" : 0.1,
    "Summary": 0.2,
    "Computer": 0.1,
    "Data": 0.6,
    "Profile": 0.1,
    "Professional Summary": 0.1,
    "Career Summary": 0.1,
    "Qualifications": 1.5,
    "Skills": 3,
    "python": 2,
    "january": 0.1,
    "August": 0.1,
    "industry": 0.1,
    "technical": 0.1,
    "exprience": 5,
    "Areas of Expertise": 0.1,
    "Key Skills": 0.1,
    "Technical Skills": 0.1,
    "Education": 6,
    "Academic Background": 0.1,
    "Professional Experience": 4,
    "Work Experience": 4,
    "javascript": 0.1,
    "Employment History": 5,
    "Relevant Experience": 0.1,
    "Projects": 0.1,
    "Certifications": 0.1,
    "Awards and Honors": 3,
    "Achievements": 2,
    "Publications": 3,
    "Languages": 1,
    "Interests": 0.1,
    "Volunteer Work": 0.1,
    "References": 0.1,
}

good_nlp = []
bad_nlp = []
# chat gpt did this method only
def evaluate_resume(resume_text, database_evaluation):
    # Tokenize and preprocess the resume
    doc = nlp(resume_text.lower())

    # Calculate the score based on keyword presence and importance
    score = sum(keywords[key] for key in keywords if key in resume_text.lower())

    # Compare the score with the database evaluation
    if score > 3.0:  # Adjust the threshold as needed
        return "good"
    else:
        return "bad"

# Example usage:
resume_text = "This is an example resume with good experience and skills."
database_evaluation = "good"  # Replace with your actual database evaluation

for resume in dataset:
    result = evaluate_resume(resume_text, database_evaluation)
    if(result == "good") : good_nlp.append(resume)
    else : bad_nlp.append(resume)
    print(f"Resume is {result}")



