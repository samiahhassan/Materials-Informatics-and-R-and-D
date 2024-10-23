
# README - Text and Table Extraction from Image and PDF documents

## Overview

This script automates the extraction of text and tables from PDFs and images, organizing the extracted data into text files for text and CSV files for tables. It utilizes various libraries to handle different formats efficiently and is designed to run on a directory of files, processing each file found and saving the results in a structured way.

## Prerequisites
Before running the script, ensure you have Python installed on your system. The script has been tested with Python 3.8 and higher.


## Installation

To set up your environment with the necessary dependencies, make sure you have Python and pip installed on your system. Then run the following command in your terminal:

```bash
pip install -r requirements.txt
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
