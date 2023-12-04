import os
from pypdf import PdfReader
import tkinter
from tkinter import filedialog
import time

def extractText(pdf_file):
    # Extract the original filename to make new one
    pdfName = os.path.splitext(pdf_file)[0]
    txtFileName = f"{pdfName}.txt"
    
    # Check if the text filename already exists to avoid overwriting
    if os.path.exists(txtFileName):
        timestamp = str(int(time.time()))
        txtFileName = f"{pdfName}_at_{timestamp}.txt"

    # Read the PDF and extract text
    with open(pdf_file, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        text = "".join(page.extract_text() or "" for page in pdf_reader.pages)

    # Write the extracted text to a file
    with open(txtFileName, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

if __name__ == "__main__":
    # Initialize tkinter for file picker
    root = tkinter.Tk()
    root.withdraw()  # Hide the main window
    
    # Show a file picker for selecting PDF files
    pdf_files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    
    # Process each selected PDF file
    for filename in pdf_files:
        extractText(filename)