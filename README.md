# Data-Extraction-and-NLP

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
mkdir Data-Extraction-and-NLP
cd Data-Extraction-and-NLP
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
   - We process the scraped text to remove stopwords from putting all the stopwords file in the `stopwords` folder each ending with `.txt`  .
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
## **6. Stopwords Folder**
In the project, we used a `stopwords` folder containing `.txt` files to remove common stopwords from the extracted articles. Each stopword file contains a list of words, and these are loaded dynamically to filter out unimportant words from the text.

## **7. Metrics Used for Sentiment and Readability Analysis**
To obtain the expected output, we used several metrics:

### 1. **Positive/Negative Score**
These scores are calculated based on the presence of positive and negative words from predefined files (`positive-words.txt` and `negative-words.txt`). Each word in the article that matches a word in these lists contributes to the positive or negative score.

### 2. **Polarity Score**
The polarity score ranges from -1 to 1, indicating whether the sentiment of the text is negative or positive. A score of 1 means the text is highly positive, and -1 means it's highly negative.

### 3. **Subjectivity Score**
This score ranges from 0 to 1, where 0 is entirely objective (factual) and 1 is completely subjective (opinion-based). It is calculated based on the use of subjective phrases and opinions in the text.

### 4. **Average Sentence Length**
The average sentence length is calculated using the formula:  
  
    
    Average Sentence Length = (Total Number of Words) / (Total Number of Sentences)
### 5. **Percentage of Complex Words**
Complex words are words that contain more than two syllables. The percentage of complex words is calculated by:
  
    
    Percentage of Complex Words = (Number of Complex Words) / (Total Number of Words)

### 6. **Fog Index**
The Fog Index is calculated using the formula:
   
    
    Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex Words)
A higher Fog Index indicates more complex text.

### 7. **Average Number of Words Per Sentence**
This is calculated by dividing the total number of words by the total number of sentences:

 
   
    Average Number of Words Per Sentence = (Total Number of Words) / (Total Number of Sentences)


### 8. **Syllable Count Per Word**
Syllable count per word is determined by counting the vowels present in each word and applying rules for exceptions like words ending in "es" or "ed." The total syllable count per word is then averaged for the entire text.
   
### 9. **Personal Pronouns**
Personal pronouns are identified using regular expressions to match the words "I," "we," "my," "ours," and "us".
   
    
    Average Sentence Length = (Total Number of Words) / (Total Number of Sentences)
### 10. **Average Word Length**
Average word length is calculated by the formula:
    
    
    Average Word Length = (Sum of the total number of characters in each word) / (Total Number of Words)



## **8. Expected Output Format**
The final Excel file `sentiment_analysis.xlsx` will have the following columns:

| Article Content | Positive Score | Negative Score | Polarity Score | Subjectivity Score | Avg Sentence Length | Percent Complex Words | Fog Index | Syllable Per Word | Personal Pronouns | Avg Word Length |
|----------------|---------------|---------------|---------------|------------------|-------------------|------------------|---------|----------------|------------------|----------------|
| "The product is excellent and well-designed." | 2 | 0 | 1.0 | 0.4 | 5.0 | 0.2 | 2.08 | 1.5 | 0 | 4.2 |
| "This is a terrible experience." | 0 | 1 | -1.0 | 0.2 | 4.0 | 0.1 | 1.64 | 1.2 | 1 | 4.0 |


## **9. Summary**
- **Extract text** using Scrapy.
- **Clean the text** (remove stopwords, punctuation, lowercase).
- **Perform sentiment analysis** (Positive/Negative Score, Polarity, Subjectivity).
- **Compute readability metrics** (Fog Index, Syllable Count, etc.).
- **Save final results** in `sentiment_analysis.xlsx`.

Now you have a complete step-by-step guide to running the project! 🚀

