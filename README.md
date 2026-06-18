# NLP Article Analysis Project

## Overview
This project performs text analysis on news articles using Natural Language Processing techniques. It's designed to extract valuable insights from text content including word frequencies, paragraph counts, and other statistical measures.

## Project Structure
nlp_article_analysis/
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├── .env.example # Environment variables template
├── src/ # Source code
│ ├── init.py
│ ├── text_analyzer.py # Core text analysis logic
│ └── file_handler.py # File I/O operations
├── data/ # Data files
│ └── news_article.txt # Input news article
├── tests/ # Unit tests
│ ├── init.py
│ └── test_analyzer.py # Test cases
├── outputs/ # Output files
│ └── analysis_results.txt # Analysis results
├── scripts/ # Utility scripts
│ └── run_analysis.py # Main execution script
└── pythonAssessment.py # Main assessment script

text

## Installation

### 1. Create Virtual Environment
```bash
python -m venv venv
2. Activate Virtual Environment
Windows:

bash
venv\Scripts\activate
Mac/Linux:

bash
source venv/bin/activate
3. Install Dependencies
bash
pip install -r requirements.txt
Usage
Running the Main Analysis
bash
python pythonAssessment.py
Running Tests
bash
pytest tests/ -v
Running with Coverage
bash
pytest tests/ --cov=src --cov-report=html
Features
Specific Word Count: Count occurrences of a specific word

Most Common Word: Identify the most frequently used word

Average Word Length: Calculate average word length

Paragraph Count: Count paragraphs based on empty lines

Sentence Count: Count sentences using punctuation marks

Configuration
Input File
Place the news article in data/news_article.txt

Search Word
The default search word is "apple". To modify:

Edit the search_word variable in pythonAssessment.py

Testing
Run the test suite:

bash
pytest tests/ -v --cov=src
Output
Results are saved to:

Console output during execution

outputs/analysis_results.txt for persistent storage

Dependencies
Python 3.8+

NLTK for NLP processing

Pandas for data handling

Pytest for testing

Troubleshooting
Common Issues
FileNotFoundError: Ensure data/news_article.txt exists

ModuleNotFoundError: Activate virtual environment and install requirements

PermissionError: Check file permissions in outputs directory

License
This project is for educational purposes as part of a Python assessment.

text

## .env.example

```env
# Environment variables for the NLP article analysis project

# Paths
DATA_DIR=./data
OUTPUT_DIR=./outputs

# Analysis settings
DEFAULT_SEARCH_WORD=apple
SENTENCE_PUNCTUATION=.!?
