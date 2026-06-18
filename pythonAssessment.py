#!/usr/bin/env python3
"""
Python Assessment - NLP Article Analysis

This script performs various text analysis tasks on a news article.
It uses the TextAnalyzer class to analyze the content of the article.
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.text_analyzer import TextAnalyzer
from src.file_handler import FileHandler
from src.utils import setup_logging, format_results, validate_text


def display_header(title: str) -> None:
    """Display a formatted header."""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def display_result(label: str, value: any, unit: str = "") -> None:
    """Display a formatted result."""
    print(f"  {label}: {value} {unit}".strip())


def main():
    """
    Main function to run the text analysis.
    """
    # Setup logging
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)
    setup_logging(log_file=str(log_dir / "analysis.log"), level="INFO")
    
    display_header("ACME Inc. News Article - Text Analysis Report")
    print(f" Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" Python Version: {sys.version.split()[0]}")
    
    try:
        # Initialize file handler and read the article
        file_handler = FileHandler()
        article_path = "data/news_article.txt"
        
        print(f"\n 📁 Reading article from: {article_path}")
        
        # Read the article content
        article_text = file_handler.read_text_file(article_path)
        
        if not validate_text(article_text):
            print("❌ Error: Invalid or empty text")
            return 1
        
        # Initialize the text analyzer
        analyzer = TextAnalyzer()
        
        # Display basic information
        print(f"\n ✅ Article loaded successfully!")
        print(f" 📊 Total characters: {len(article_text):,}")
        print(f" 📊 Characters (no spaces): {len(article_text.replace(' ', '').replace('\\n', '')):,}")
        
        # Store all results for formatting
        results = {}
        
        # 1. Count specific word
        display_header("1. Specific Word Count")
        search_word = "apple"
        count = analyzer.count_specific_word(article_text, search_word)
        results['search_word_count'] = count
        display_result(f"Occurrences of '{search_word}'", count)
        
        # Additional specific words
        additional_words = ["pie", "baking", "technology", "ACME", "machine"]
        print("\n  📝 Additional word counts:")
        for word in additional_words:
            word_count = analyzer.count_specific_word(article_text, word)
            results[f'count_{word}'] = word_count
            print(f"    '{word}': {word_count}")
        
        # 2. Most common word
        display_header("2. Most Common Word")
        most_common = analyzer.identify_most_common_word(article_text)
        results['most_common_word'] = most_common
        display_result("Most common word", f"'{most_common}'")
        
        # 3. Average word length
        display_header("3. Average Word Length")
        avg_length = analyzer.calculate_average_word_length(article_text)
        results['avg_word_length'] = avg_length
        display_result("Average word length", avg_length, "characters")
        
        # 4. Number of paragraphs
        display_header("4. Paragraph Count")
        paragraph_count = analyzer.count_paragraphs(article_text)
        results['total_paragraphs'] = paragraph_count
        display_result("Total paragraphs", paragraph_count)
        
        # 5. Number of sentences
        display_header("5. Sentence Count")
        sentence_count = analyzer.count_sentences(article_text)
        results['total_sentences'] = sentence_count
        display_result("Total sentences", sentence_count)
        
        # 6. Additional statistics
        display_header("6. Comprehensive Statistics")
        stats = analyzer.get_text_statistics()
        
        # Merge stats with results
        results.update(stats)
        
        # Display stats
        stat_items = [
            ("Total words", stats.get('total_words', 0)),
            ("Unique words", stats.get('unique_words', 0)),
            ("Total paragraphs", stats.get('total_paragraphs', 0)),
            ("Total sentences", stats.get('total_sentences', 0)),
        ]
        
        for label, value in stat_items:
            display_result(label, f"{value:,}")
        
        # Display word frequency
        print("\n  📊 Top 10 Most Frequent Words:")
        for word, count in stats.get('word_frequency', [])[:10]:
            print(f"    {word}: {count}")
        
        # Save results to file
        display_header("💾 Saving Results")
        
        # Format and save results
        output_content = format_results(results, search_word, additional_words)
        output_path = "outputs/analysis_results.txt"
        
        # Create outputs directory if it doesn't exist
        Path(output_path).parent.mkdir(exist_ok=True)
        
        file_handler.write_results(output_path, output_content)
        
        display_header("✅ Analysis Complete!")
        print("\n 📄 Results have been saved to:", output_path)
        print(" 📁 Log file: logs/analysis.log")
        print(" 👋 Thank you for using the NLP Article Analysis Tool!")
        
    except FileNotFoundError as e:
        print(f"\n ❌ ERROR: {e}")
        print("\n Please ensure the data/news_article.txt file exists.")
        print(" You can create it by copying the article content from the document.")
        return 1
    except Exception as e:
        print(f"\n ❌ ERROR: An unexpected error occurred: {e}")
        print(f" Error type: {type(e).__name__}")
        
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())