# Data-Extraction-and-NLP
# Sentiment Analysis & Readability Metrics Project

## **Overview**
This project extracts article content from multiple websites using Scrapy, cleans the text by removing stopwords, and performs sentiment and readability analysis. The final output is saved in an Excel file.

## **1. Install Required Dependencies**
Ensure you have Python installed, then install the required libraries:

```bash
pip install scrapy nltk pandas openpyxl
```

If Scrapy is not installed:

```bash
pip install scrapy
```

## **2. Set Up the Project**
Create a new directory for the project and navigate into it:

```bash
mkdir sentiment_analysis_project
cd sentiment_analysis_project
```

Initialize a Scrapy project:

```bash
scrapy startproject article_scraper
```

Navigate to the Scrapy project directory:

```bash
cd article_scraper
```

Place your spider script inside the `spiders/` folder.

## **3. Approach to the Solution**
1. **Scraping Articles Using Scrapy**  
   - We use Scrapy to crawl the given websites and extract article content.  
   - Extracted data is saved in `extracted_articles.xlsx`.

2. **Cleaning Extracted Text**  
   - We process the scraped text to remove stopwords from `stopwords.txt`.
   - The text is tokenized, converted to lowercase, and unnecessary punctuation is removed.
   - Cleaned data is saved in `cleaned_articles.xlsx`.

3. **Performing Sentiment Analysis & Readability Metrics Calculation**  
   - Positive and Negative words are identified using `positive-words.txt` and `negative-words.txt`.
   - We compute polarity and subjectivity scores.
   - Readability metrics such as Average Sentence Length, Fog Index, and Syllable Count Per Word are calculated.
   - The final output is saved in `sentiment_analysis.xlsx`.

## **4. Running the Python Scripts**

### **Run the Scrapy Spider to Extract Articles**
```bash
scrapy crawl article_spider -o extracted_articles.xlsx
```

### **Run the Text Cleaning Script**
```bash
python clean_text.py
```

### **Run Sentiment Analysis & Readability Metrics Calculation**
```bash
python sentiment_analysis.py
```

## **5. Dependencies Required**
The following dependencies are required for the project:

```txt
Python 3.x
Scrapy
NLTK
Pandas
OpenPyXL
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## **6. Expected Output Format**
The final Excel file `sentiment_analysis.xlsx` will have the following columns:

| Article Content | Positive Score | Negative Score | Polarity Score | Subjectivity Score | Avg Sentence Length | Percent Complex Words | Fog Index | Syllable Per Word | Personal Pronouns | Avg Word Length |
|----------------|---------------|---------------|---------------|------------------|-------------------|------------------|---------|----------------|------------------|----------------|
| "The product is excellent and well-designed." | 2 | 0 | 1.0 | 0.4 | 5.0 | 0.2 | 2.08 | 1.5 | 0 | 4.2 |
| "This is a terrible experience." | 0 | 1 | -1.0 | 0.2 | 4.0 | 0.1 | 1.64 | 1.2 | 1 | 4.0 |

## **7. Troubleshooting Common Issues**

1. **Scrapy Output Format Error**  
   - Ensure the output format is compatible (`.json`, `.csv`, `.xml`, `.xlsx`).  
   - If using `.xlsx`, use **pandas** to convert the output.

2. **Module Not Found (`article_scraper`)**
   - Run the script from the correct directory.
   - Use `sys.path.append()` in Python to add missing module paths.

3. **Encoding Errors (`'utf-8' codec can't decode byte` Error)**
   - Open text files with encoding handling:
     ```python
     with open("stopwords.txt", "r", encoding="utf-8", errors="ignore") as f:
         stopwords = f.read().splitlines()
     ```

4. **Scrapy Not Extracting Content**
   - Ensure the correct **CSS/XPath selectors** are used.
   - Check if the website requires **headers or cookies** for access.

## **8. Running the Full Pipeline in One Go**
To automate the entire process, create a shell script `run_pipeline.sh` (Linux/macOS):

```bash
#!/bin/bash

scrapy crawl article_spider -o extracted_articles.xlsx
python clean_text.py
python sentiment_analysis.py
```

Run it using:

```bash
bash run_pipeline.sh
```

For Windows, create a batch script `run_pipeline.bat`:

```batch
@echo off
scrapy crawl article_spider -o extracted_articles.xlsx
python clean_text.py
python sentiment_analysis.py
```

Run it by executing:

```cmd
run_pipeline.bat
```

## **9. Summary**
- **Extract text** using Scrapy.
- **Clean the text** (remove stopwords, punctuation, lowercase).
- **Perform sentiment analysis** (Positive/Negative Score, Polarity, Subjectivity).
- **Compute readability metrics** (Fog Index, Syllable Count, etc.).
- **Save final results** in `sentiment_analysis.xlsx`.

Now you have a complete step-by-step guide to running the project! 🚀

