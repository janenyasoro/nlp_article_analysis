#!/usr/bin/env python3
"""
Script to run the analysis with different parameters.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.text_analyzer import TextAnalyzer
from src.file_handler import FileHandler
from src.utils import setup_logging


def run_analysis_with_word(search_word: str):
    """
    Run analysis with a specific search word.
    """
    print(f"\n{'='*60}")
    print(f"🔍 Running analysis with search word: '{search_word}'")
    print('='*60)
    
    try:
        # Setup logging
        setup_logging(level="INFO")
        
        file_handler = FileHandler()
        article_path = "data/news_article.txt"
        article_text = file_handler.read_text_file(article_path)
        
        analyzer = TextAnalyzer()
        
        # Count specific word
        count = analyzer.count_specific_word(article_text, search_word)
        print(f"📝 Occurrences of '{search_word}': {count}")
        
        # Most common word
        most_common = analyzer.identify_most_common_word(article_text)
        print(f"🏆 Most common word: '{most_common}'")
        
        # Average word length
        avg_length = analyzer.calculate_average_word_length(article_text)
        print(f"📏 Average word length: {avg_length:.2f} characters")
        
        # Paragraph count
        paragraphs = analyzer.count_paragraphs(article_text)
        print(f"📄 Total paragraphs: {paragraphs}")
        
        # Sentence count
        sentences = analyzer.count_sentences(article_text)
        print(f"📝 Total sentences: {sentences}")
        
        # Get word frequency
        word_freq = analyzer.get_word_frequency(article_text, 5)
        print("\n📊 Top 5 Most Frequent Words:")
        for word, freq in word_freq:
            print(f"  {word}: {freq}")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    """Run analysis with multiple search words."""
    # Different search words to test
    search_words = ["apple", "pie", "baking", "technology", "ACME", "Inc", "machine"]
    
    for word in search_words:
        run_analysis_with_word(word)
        print("\n" + "-"*60)


if __name__ == "__main__":
    main()