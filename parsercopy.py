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

# Provide the path to the PDF resume
# file_path = input("Enter the path to the PDF resume file: ")

# # output file
# output_file_path = "parsed_resume.txt"

# # Parse the PDF resume
# parsed_text = parse_pdf_resume(file_path)

# Display the parsed text
# # print("Parsed Text from PDF Resume:")
# # print(parsed_text)
