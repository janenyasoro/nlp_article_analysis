"""
Utility functions for the NLP article analysis project.
"""

import re
import logging
import sys
from typing import List, Optional
from pathlib import Path


def setup_logging(log_file: Optional[str] = None, level: str = "INFO") -> None:
    """
    Set up logging configuration.
    
    Args:
        log_file (str, optional): Path to log file
        level (str): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    log_level = getattr(logging, level.upper())
    
    handlers = [logging.StreamHandler(sys.stdout)]
    
    if log_file:
        # Create log directory if it doesn't exist
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_file))
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )


def validate_text(text: str) -> bool:
    """
    Validate if the text is valid for analysis.
    
    Args:
        text (str): Text to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not text:
        return False
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    return True


def extract_keywords(text: str, min_word_length: int = 3) -> List[str]:
    """
    Extract keywords from text.
    
    Args:
        text (str): Text to extract keywords from
        min_word_length (int): Minimum word length to include
        
    Returns:
        List[str]: List of keywords
    """
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter by minimum length and remove stopwords
    stopwords = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'to', 'for',
                 'of', 'and', 'or', 'but', 'in', 'on', 'at', 'with', 'without'}
    
    keywords = [w for w in words if len(w) >= min_word_length and w not in stopwords]
    
    return keywords


def clean_text(text: str) -> str:
    """
    Clean text by removing extra whitespace and special characters.
    
    Args:
        text (str): Text to clean
        
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove special characters but keep punctuation
    cleaned = re.sub(r'[^\w\s\.\?!,\'"]', ' ', text)
    
    return cleaned


def format_results(stats: dict, search_word: str, additional_words: List[str] = None) -> str:
    """
    Format analysis results for output.
    
    Args:
        stats (dict): Statistics dictionary
        search_word (str): The search word used
        additional_words (List[str], optional): Additional words to count
        
    Returns:
        str: Formatted results
    """
    from datetime import datetime
    
    output = f"""
NLP Article Analysis Results
============================
Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

1. Specific Word Count
   Occurrences of '{search_word}': {stats.get('search_word_count', 0)}
"""
    
    if additional_words:
        output += "\n   Additional word counts:\n"
        for word in additional_words:
            output += f"    '{word}': {stats.get(f'count_{word}', 0)}\n"
    
    output += f"""
2. Most Common Word
   Most common word: '{stats.get('most_common_word', 'N/A')}'

3. Average Word Length
   Average word length: {stats.get('avg_word_length', 0.0)} characters

4. Paragraph Count
   Total paragraphs: {stats.get('total_paragraphs', 0)}

5. Sentence Count
   Total sentences: {stats.get('total_sentences', 0)}

6. Additional Statistics
   Total words: {stats.get('total_words', 0)}
   Unique words: {stats.get('unique_words', 0)}
   Total characters: {stats.get('total_characters', 0)}
   
7. Word Frequency (Top 10)
"""
    
    for word, count in stats.get('word_frequency', []):
        output += f"   {word}: {count}\n"
    
    return output