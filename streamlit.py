import pandas as pd
import spacy
import streamlit as st
import PyPDF2

nlp = spacy.load("en_core_web_sm")
def parse_pdf_resume(file_path):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file_path)
    
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text

def calculate_keyword_percentage(resume_text, resume_keywords):
    total_sum = len(resume_keywords)
    total_amt = 0
    
    for word in resume_text.split():
        if word in resume_keywords:
            total_amt += 1

    return (float)(total_amt / total_sum) * 100

def evaluate_resume(resume_text, keywords, threshold=3.0):
    doc = nlp(resume_text.lower())
    score = sum(keywords[key] for key in keywords if key in resume_text.lower())
    return "good" if score > threshold else "bad"

def main():
    # Load spaCy's English language model
    

    st.title("Resume Uploader and Processor")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    user_input = st.text_area("Paste or type your resume here:")

    if st.button("Process Resume"):
        if user_input:
            df = pd.DataFrame({'Resume': [user_input]})
        elif uploaded_file:
            resume_text = parse_pdf_resume(uploaded_file)
            df = pd.DataFrame({'Resume': [resume_text]})
        else:
            st.warning("Please enter your resume text or upload a PDF file.")

        dataset = df['Resume']
        dataset = dataset.str.lower()

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

        resume_keywords = {value.lower(): 1 for value in resume_keys}
        
        percentage_array = [calculate_keyword_percentage(resume, resume_keywords) for resume in dataset]
        
        good_resumes = [resume for resume, percent in zip(dataset, percentage_array) if percent >= 30]
        bad_resumes = [resume for resume, percent in zip(dataset, percentage_array) if percent < 30]

        # st.write("Length good:", len(good_resumes))
        # st.write("Length bad:", len(bad_resumes))

        for resume in dataset:
            result = evaluate_resume(resume, resume_keywords)
            st.write(f"Resume is {result}")

if __name__ == "__main__":
    main()




# import streamlit as st;


# st.title("Resume Uploader and Processor")

# uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# if uploaded_file:
#     st.success("File successfully uploaded")

# # using sample function here, will connect to backend later

# # for now it will just show parsed text instead of score

# import PyPDF2

# # Function to parse a PDF resume
# def parse_pdf_resume(file_path):
#     text = ""
#     pdf_reader = PyPDF2.PdfReader(file_path)
    
#     # Loop through each page and extract text
#     for page_num in range(len(pdf_reader.pages)):
#         page = pdf_reader.pages[page_num]
#         text += page.extract_text()

#     return text

# if uploaded_file:
#     resume_text = parse_pdf_resume(uploaded_file)
#     st.write("Extracted Text from Resume:")
#     st.text(resume_text)


