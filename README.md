
# README - Text and Table Extraction from Image and PDF documents

## Overview

This script automates the extraction of text and tables from PDFs and images, organizing the extracted data into text files for text and CSV files for tables. It utilizes various libraries to handle different formats efficiently and is designed to run on a directory of files, processing each file found and saving the results in a structured way.

## Prerequisites
Before running the script, ensure you have Python installed on your system. The script has been tested with Python 3.8 and higher.


## Installation

To set up your environment with the necessary dependencies, make sure you have Python and pip installed on your system. Then run the following command in your terminal:

```bash
pip install -r requirements.txt

To run the script, you need to install several dependencies. Here is the step-by-step guide to install all required libraries:

1. **OpenCV** (for image processing):
   ```bash
   pip install opencv-python
   ```
2. **Pillow** (PIL fork, for image manipulation):
   ```bash
   pip install pillow
   ```
3. **PaddleOCR** (for optical character recognition):
   ```bash
   pip install paddleocr
   ```
4. **PaddlePaddle** (dependencies for PaddleOCR):
   ```bash
   pip install paddlepaddle
   ```
5. **NumPy** (ensure version is compatible):
   ```bash
   pip install 'numpy<2.0'
   ```
6. **Albumentations** (for augmenting images, used in pre-processing):
   ```bash
   pip install albumentations
   ```
7. **pdfplumber** (for extracting text from PDF files):
   ```bash
   pip install pdfplumber
   ```
8. **Tabula** (for extracting tables from PDF files):
   ```bash
   pip install tabula
   pip install tabula-py
   ```
9. **Pandas** (for handling data and saving in CSV format):
   ```bash
   pip install pandas
   ```
10. **Premailer** (for converting web content to inline CSS, useful for email processing):
    ```bash
    pip install premailer
    ```
11. **OpenPyXL** (for handling Excel files, if needed):
    ```bash
    pip install openpyxl
    ```

## Running the Script

After installing all the necessary packages, you can run the script by following these steps:

1. Place the script in a directory containing the PDF and image files you want to process.
2. Open a command prompt or terminal in this directory.
3. Run the script by typing:
   ```bash
   python Extraction.py
   ```


## Output

The script will process each file in the directory, extracting text to `.txt` files and tables to `.csv` files. Results will be organized into subfolders for each processed file, located within the directory you ran the script in.
