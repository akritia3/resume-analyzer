import streamlit as st
import PyPDF2
import base64
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
        # words = get_most_used_words('UpdatedResumeDataSet.csv')
        # missing = getMissingWords(parsed_text, words)

        st.header("Resume Analysis Results")
        st.write("Your Resume Score: ", result)
        # st.write("Words that could maek your resume better: ", missing)
        st.write(
            "The resume score is calculated based on the presence of key terms and phrases "
            "found in a well-constructed resume. The model analyzes factors such as skills, "
            "experience, and education to determine the overall quality of the resume. "
            "A score above 25 is indicative of a strong resume."
        )

        if result[0] == "Bad resume":
            st.header("Improvement Suggestions")
            st.write("Here are some samples of good resumes for ideas to improve:")

            # Replace the image paths below with the actual paths of your images
            image_paths = ["image1.png", "image2.png"]

            # Display images in a horizontal row
            for i, image_path in enumerate(image_paths, start=1):
            # Add the "fullscreenable" class to each image
                # st.image(image_path, caption=f"Example {i}", width=200)
                st.write(f"Example{i}")

                pdf_file_path = f"image{i}.pdf"  # Corrected line with f-string

                pdf_embed = f'<iframe src="data:application/pdf;base64,{base64.b64encode(open(pdf_file_path, "rb").read()).decode()}" width="100%" height="600px"></iframe>'
                st.markdown(pdf_embed, unsafe_allow_html=True)

if __name__ == "__main__":
    main()




