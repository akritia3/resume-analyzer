import streamlit as st
import PyPDF2
import csv
from collections import Counter
import os
import pandas as pd
from Word_tokenizer import *
from Model_data import *
from parsercopy import *

# Streamlit app
# Some chatgpt help here for loading the input file
def main():
    st.title("Resume Analyzer")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Define the directory to store uploaded files
        upload_directory = "uploads"
        os.makedirs(upload_directory, exist_ok=True)

        # Create a unique file name (e.g., using the original file name)
        file_name = uploaded_file.name
        file_path = os.path.join(upload_directory, file_name)

        # Save the uploaded file to the specified path
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())


        parsed_text = parse_pdf_resume(file_path)
        result = assess_resume(parsed_text)

        st.header("Resume Analysis Results")
        st.write("Your Resume Score: ", result)
        st.write(
            "The resume score is calculated based on the presence of key terms and phrases "
            "found in a well-constructed resume. The model analyzes factors such as skills, "
            "experience, and education to determine the overall quality of the resume. "
            "A score above 25 is indicative of a strong resume."
        )

if __name__ == "__main__":
    main()




