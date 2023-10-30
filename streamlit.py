import streamlit as st;


st.title("Resume Uploader and Processor")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    st.success("File successfully uploaded")

# using sample function here, will connect to backend later

# for now it will just show parsed text instead of score

import PyPDF2

# Function to parse a PDF resume
def parse_pdf_resume(file_path):
    text = ""
    pdf_reader = PyPDF2.PdfReader(file_path)
    
    # Loop through each page and extract text
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text

if uploaded_file:
    resume_text = parse_pdf_resume(uploaded_file)
    st.write("Extracted Text from Resume:")
    st.text(resume_text)


