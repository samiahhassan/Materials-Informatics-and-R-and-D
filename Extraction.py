"""
This script automates the extraction of text and tables from PDFs and images, saving the data in text and CSV formats. 
It processes all files within a specified directory, organizing outputs into corresponding subfolders for easy retrieval. 
The script utilizes PaddleOCR for OCR tasks, pdfplumber for extracting text from PDFs, and tabula-py for table extraction,
ensuring comprehensive data handling from various document formats.
"""


# Import necessary libraries and modules for image and PDF processing, OCR capabilities, and system operations.
import os
import cv2
from PIL import Image
from paddleocr import PPStructure, draw_structure_result, save_structure_res
import pdfplumber
import tabula
import pandas as pd
from paddleocr import PaddleOCR
import platform


# Extracting table and text from PDF
def process_pdf(pdf_path, output_root):
    # Extract the base filename without its extension from the provided PDF path, used for naming output files.
    pdf_base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Define and create directories to store CSV and text outputs from the PDF
    csv_output = os.path.join(output_root, 'CSV_PDF', pdf_base_name)
    text_output = os.path.join(output_root, 'Text_PDF', pdf_base_name)
    os.makedirs(csv_output, exist_ok=True)
    os.makedirs(text_output, exist_ok=True)

    # Open the PDF file using the pdfplumber library
    with pdfplumber.open(pdf_path) as pdf:
        # Count the total number of pages in the PDF
        total_pages = len(pdf.pages) 
        for page_number in range(total_pages):
            # Get a specific page by index
            page = pdf.pages[page_number]  
            # Extract all text from the current page
            text = page.extract_text()

            # If text is extracted, write it to a file in the designated text output directory
            if text:
                text_filename = f"{pdf_base_name}_page_{page_number+1}.txt"
                text_path = os.path.join(text_output, text_filename)
                with open(text_path, 'w', encoding='utf-8-sig') as text_file:
                    text_file.write(text)
                print(f"Saved text: {text_path}")

            # Use Tabula to read tables from the current page of the PDF and return a list of DataFrames
            df_list = tabula.read_pdf(pdf_path, pages=page_number+1, stream= True, multiple_tables=True)
            for i, df in enumerate(df_list):
                # Save each table as a CSV file in the designated CSV output directory
                table_filename = f"{pdf_base_name}_page_{page_number+1}_table_{i+1}.csv"
                table_path = os.path.join(csv_output, table_filename)
                df.to_csv(table_path, index=False, encoding='utf-8-sig')
                print(f"CSV file Saved: {table_path}")


# Extracting text and table from the image
def process_image(image_path, output_root):
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Initialize PaddleOCR to detect text, considering orientation and language
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')

    # Initialize PPStructure for extracting tables with specific configurations
    table_engine= PPStructure(table=True, show_log=True, ocr=True, image_orientation=False, recovery=True,layout=True)
    
    # Apply the table extraction model to the image
    result = table_engine(img)

    # Apply the OCR model to extract text
    ocr_result = ocr.ocr(image_path, cls=True)

    # Prepare directory to save OCR and structured results
    image_base_name = os.path.splitext(os.path.basename(image_path))[0]
    save_folder = os.path.join(output_root, 'OCR_Output', image_base_name)
    os.makedirs(save_folder, exist_ok=True)
    save_structure_res(result, save_folder, image_base_name)

    #layout analysis
    for line in result:
        line.pop('img')
    
    # Setup the font path based on operating system for displaying the structured results
    if platform.system() == 'Windows':
        font_path = 'doc/fonts/simfang.ttf'
    else:
        font_path = '/System/Library/Fonts/STHeiti Light.ttc'
     
    # Draw and save the structured results on the image
    image = Image.open(image_path).convert('RGB')
    im_show = draw_structure_result(image, result, font_path=font_path)
    im_show = Image.fromarray(im_show)
    save_path = os.path.join(save_folder, f'{image_base_name}_result.jpg')
    im_show.save(save_path)
    #print(f"Processed image saved at {save_path}")

    # Initialize an empty string to hold the extracted text
    text_file_path = os.path.join(save_folder, f'{image_base_name}_OCR.txt')
    extracted_text = ""

    # Process each OCR result and save the extracted text simultaneously
    for res in ocr_result:
        for line in res:
            text = line[1][0]
            extracted_text += text + '\n'
    with open(text_file_path, 'w', encoding='utf-8-sig') as text_file:
        text_file.write(extracted_text)
    print(f"Extracted text saved at: {text_file_path}")

def main():
    # Get the current working directory and prepare the output root directory
    script_dir = os.getcwd()
    output_root = os.path.join(script_dir, 'Output')

    # Process each file in the directory, check if it's a PDF or image and apply the appropriate processing
    files = os.listdir(script_dir)
    for file in files:
        file_path = os.path.join(script_dir, file)
        if file.lower().endswith('.pdf'):
            print(f"PDF file {file} processed")
            process_pdf(file_path, output_root)
        elif file.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Image {file} processed")
            process_image(file_path, output_root)

if __name__ == "__main__":
    main()