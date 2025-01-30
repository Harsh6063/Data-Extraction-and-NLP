import scrapy
import pandas as pd
import os

class ArticleSpider(scrapy.Spider):
    name = "articles"

    # Load URLs from an Excel file
    input_file = "input.xlsx"
    output_file = "extracted_articles.xlsx"

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File {input_file} not found.")

    df = pd.read_excel(input_file)

    if 'URL' not in df.columns:
        raise ValueError("The Excel file must contain a column named 'URL'")

    start_urls = df["URL"].dropna().tolist()  # Remove empty URLs

    custom_settings = {
        'FEEDS': {
            'extracted_articles.csv': {'format': 'csv'},  # Save as CSV first
        }
    }

    def parse(self, response):
        title = response.xpath('//title/text()').get(default="Title Not Found").strip()
        
        # Extract main article content (try common article tags first)
        article_content = " ".join(response.xpath('//article//p//text()').getall()).strip()

        # If no content is found, extract from <div>, <section>, or main <p> tags
        if not article_content:
            article_content = " ".join(response.xpath('//div[contains(@class, "content") or contains(@class, "article")]//p//text()').getall()).strip()
        if not article_content:
            article_content = " ".join(response.xpath('//section//p//text()').getall()).strip()
        if not article_content:
            article_content = " ".join(response.xpath('//p//text()').getall()[:5]).strip()  # First 5 paragraphs

        yield {
            "URL": response.url,
            "Article Title": title,
            "Article Content": article_content if article_content else "Content Not Found"
        }

    def closed(self, reason):
        """Convert CSV to Excel when Scrapy finishes"""
        csv_file = "extracted_articles.csv"
        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            df.to_excel(self.output_file, index=False)
            print(f"✅ Excel file saved: {self.output_file}")
from scrapy.crawler import CrawlerProcess
from article_scraper.spiders.article_spider import ArticleSpider

process = CrawlerProcess(settings={
    "FEEDS": {
        "extracted_articles.csv": {"format": "csv"},
    },
})

process.crawl(ArticleSpider)
process.start()

import pandas as pd
import os
import re

# Load extracted articles
input_file = "extracted_articles.xlsx"
output_file = "cleaned_articles.xlsx"
stopwords_folder = "stopwords/"

# Read all stopwords from multiple text files
# Read all stopwords from multiple text files
def load_stopwords(folder):
    stopwords = set()
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()  # Read entire file
                words = content.replace("\n", " ").split()  # Split on spaces and newlines
                stopwords.update(word.lower() for word in words)  # Convert to lowercase
    return stopwords

# Function to clean text by removing stopwords
def clean_text(text, stopwords):
    words = text.split()  # Tokenize words
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return " ".join(filtered_words)

# Load data
df = pd.read_excel(input_file)

# Ensure 'Article Content' column exists
if "Article Content" not in df.columns:
    raise ValueError("The Excel file must contain a column named 'Article Content'")

# Load stopwords
stopwords = load_stopwords(stopwords_folder)
print(f"Loaded {len(stopwords)} stopwords.")

# Clean the 'Article Content' column
df["Article Content"] = df["Article Content"].astype(str).apply(lambda text: clean_text(text, stopwords))

# Save cleaned data
df.to_excel(output_file, index=False)
print(f"Cleaned data saved to {output_file}")

import pandas as pd
import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize


# Load Positive and Negative words
def load_words(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        words = f.read().lower().split()  # Convert to lowercase and split words
    return set(words)

positive_words = load_words("positive-words.txt")
negative_words = load_words("negative-words.txt")

# Function to clean text and tokenize
def clean_and_tokenize(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    tokens = word_tokenize(text.lower())  # Convert to lowercase and tokenize
    return tokens

# Function to count syllables in a word
def count_syllables(word):
    word = word.lower()
    vowels = "aeiou"
    count = sum(1 for char in word if char in vowels)  # Count vowels
    if word.endswith(("es", "ed")):  # Ignore certain suffixes
        count -= 1
    return max(1, count)  # Ensure at least one syllable

# Function to count personal pronouns
def count_personal_pronouns(text):
    pronouns = ["i", "we", "my", "ours", "us"]
    return sum(1 for word in word_tokenize(text.lower()) if word in pronouns and word != "us")  # Exclude 'US' (country)

# Function to calculate all required metrics
def calculate_scores(text):
    sentences = sent_tokenize(text)
    words = clean_and_tokenize(text)
    total_words = len(words)
    total_sentences = len(sentences)

    pos_score = sum(1 for word in words if word in positive_words)
    neg_score = sum(1 for word in words if word in negative_words)

    polarity_score = (pos_score - neg_score) / ((pos_score + neg_score) + 0.000001)
    subjectivity_score = (pos_score + neg_score) / (total_words + 0.000001)

    # Readability Metrics
    avg_sentence_length = total_words / total_sentences if total_sentences > 0 else 0
    complex_words = [word for word in words if count_syllables(word) > 2]
    percent_complex_words = len(complex_words) / total_words if total_words > 0 else 0
    fog_index = 0.4 * (avg_sentence_length + percent_complex_words)

    avg_words_per_sentence = total_words / total_sentences if total_sentences > 0 else 0
    syllable_per_word = sum(count_syllables(word) for word in words) / total_words if total_words > 0 else 0

    personal_pronouns = count_personal_pronouns(text)
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0

    return [
        pos_score, neg_score, polarity_score, subjectivity_score,
        avg_sentence_length, percent_complex_words, fog_index,
        avg_words_per_sentence, syllable_per_word, personal_pronouns, avg_word_length
    ]

# Load Excel data
input_file = "cleaned_articles.xlsx"
output_file = "sentiment_analysis.xlsx"

df = pd.read_excel(input_file)

# Ensure 'Article Content' column exists
if "Article Content" not in df.columns:
    raise ValueError("The Excel file must contain a column named 'Article Content'")

# Apply sentiment analysis & readability metrics
df[
    [
        "Positive Score", "Negative Score", "Polarity Score", "Subjectivity Score",
        "Avg Sentence Length", "Percent Complex Words", "Fog Index",
        "Avg Words Per Sentence", "Syllable Per Word", "Personal Pronouns", "Avg Word Length"
    ]
] = df["Article Content"].astype(str).apply(lambda text: pd.Series(calculate_scores(text)))

# Save results
df.to_excel(output_file, index=False)
print(f"Sentiment analysis & readability metrics saved in '{output_file}'.")
