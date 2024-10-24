
# README - Text and Table Extraction from Image and PDF documents

## Overview

This script automates the extraction of text and tables from PDFs and images, organizing the extracted data into text files for text and CSV and Excel files for tables. It utilizes various libraries to handle different formats efficiently and is designed to run on a directory of files, processing each file found and saving the results in a structured way.

## Prerequisites
Before running the script, ensure you have Python installed on your system. The script has been tested with Python 3.8 and higher.


## Installation

To set up your environment with the necessary dependencies, make sure you have Python and pip installed on your system. Then run the following command in your terminal:

```bash
pip install -r requirements.txt
```
## Running the Script

After installing all the necessary packages, you can run the script by following these steps:

1. Set the input directory in the script to the folder containing the PDF and image files you want to process. Replace `'/your/input_directory'` in the script with the path to your specific folder. This setup does not use an environment variable; instead, it relies on direct modification within the script.
2. Open a command prompt or terminal in this directory.
3. Run the script by typing:
   ```bash
   python Extraction.py
   ```


## Output

The script will process each file in the directory, extracting text to `.txt` files and tables to `.csv` files. Results will be organized into subfolders for each processed file, located within the directory you ran the script in. For guidance on expected output formats and organization, please refer to the "Extraction.pptx" PowerPoint file included in the directory. This presentation provides a clear example of how output files are structured and named.
