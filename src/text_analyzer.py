"""
Text analysis module for processing news articles.
"""

import re
import string
import logging
from collections import Counter
from typing import Optional, List, Dict, Tuple

logger = logging.getLogger(__name__)


class TextAnalyzer:
    """
    Analyzes text content for various metrics.
    
    This class provides methods for counting words, identifying most common words,
    calculating average word length, and counting paragraphs and sentences.
    """
    
    def __init__(self, text: str = ""):
        """
        Initialize the TextAnalyzer with text content.
        
        Args:
            text (str): The text to analyze
        """
        self.text = text
        self._words = None
        self._sentences = None
        self._paragraphs = None
        
        if text:
            self._preprocess_text()
            
    def _preprocess_text(self) -> None:
        """Preprocess the text for analysis."""
        if self.text:
            # Clean the text
            self.text = self._clean_text(self.text)
            
    def _clean_text(self, text: str) -> str:
        """
        Clean the text by removing special characters and extra whitespace.
        
        Args:
            text (str): Input text
            
        Returns:
            str: Cleaned text
        """
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Keep letters, numbers, spaces, and basic punctuation
        cleaned = re.sub(r'[^\w\s\.\?!,\'"]', ' ', text)
        
        return cleaned
        
    def set_text(self, text: str) -> None:
        """
        Set the text to be analyzed.
        
        Args:
            text (str): The text to analyze
        """
        self.text = text
        self._words = None
        self._sentences = None
        self._paragraphs = None
        
        if text:
            self._preprocess_text()
            
    def count_specific_word(self, text: str, search_word: str) -> int:
        """
        Count occurrences of a specific word in the text using a while loop.
        
        Args:
            text (str): The text to search through
            search_word (str): The word to count
            
        Returns:
            int: Number of occurrences
            
        Examples:
            >>> analyzer = TextAnalyzer()
            >>> analyzer.count_specific_word("Hello world hello", "hello")
            2
        """
        if not text or not search_word:
            return 0
            
        # Convert to lowercase for case-insensitive matching
        text_lower = text.lower()
        search_word_lower = search_word.lower()
        
        # Split text into words
        words = re.findall(r'\b\w+\b', text_lower)
        
        # Use a while loop to count occurrences
        count = 0
        i = 0
        while i < len(words):
            if words[i] == search_word_lower:
                count += 1
            i += 1
        
        logger.debug(f"Found '{search_word}' {count} times")
        
        return count
        
    def identify_most_common_word(self, text: str) -> Optional[str]:
        """
        Identify the most common word in the text using a while loop.
        
        Args:
            text (str): The text to analyze
            
        Returns:
            Optional[str]: Most common word or None if empty
            
        Examples:
            >>> analyzer = TextAnalyzer()
            >>> analyzer.identify_most_common_word("hello world hello")
            "hello"
        """
        if not text or not text.strip():
            return None
            
        # Clean the text and remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        cleaned = text.translate(translator)
        
        # Split into words and convert to lowercase
        words = cleaned.lower().split()
        
        if not words:
            return None
            
        # Use a while loop to count word frequencies
        word_counts = {}
        i = 0
        while i < len(words):
            word = words[i]
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
            i += 1
        
        # Find the most common word using a while loop
        max_count = 0
        most_common_word = None
        word_list = list(word_counts.items())
        j = 0
        while j < len(word_list):
            word, count = word_list[j]
            if count > max_count:
                max_count = count
                most_common_word = word
            j += 1
        
        result = most_common_word
        logger.debug(f"Most common word: {result}")
        
        return result
        
    def get_word_frequency(self, text: str, top_n: int = 10) -> List[Tuple[str, int]]:
        """
        Get the frequency of the most common words.
        
        Args:
            text (str): The text to analyze
            top_n (int): Number of top words to return
            
        Returns:
            List[Tuple[str, int]]: List of (word, count) tuples
        """
        if not text or not text.strip():
            return []
            
        translator = str.maketrans('', '', string.punctuation)
        cleaned = text.translate(translator)
        words = cleaned.lower().split()
        
        if not words:
            return []
        
        # Use a while loop to count word frequencies
        word_counts = {}
        i = 0
        while i < len(words):
            word = words[i]
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
            i += 1
        
        # Convert to list of tuples and sort using while loop
        freq_list = list(word_counts.items())
        
        # Simple bubble sort using while loops
        n = len(freq_list)
        i = 0
        while i < n - 1:
            j = 0
            while j < n - i - 1:
                if freq_list[j][1] < freq_list[j + 1][1]:
                    # Swap
                    freq_list[j], freq_list[j + 1] = freq_list[j + 1], freq_list[j]
                j += 1
            i += 1
        
        return freq_list[:top_n]
        
    def calculate_average_word_length(self, text: str) -> float:
        """
        Calculate the average length of words in the text.
        
        Args:
            text (str): The text to analyze
            
        Returns:
            float: Average word length rounded to 2 decimal places
            
        Examples:
            >>> analyzer = TextAnalyzer()
            >>> analyzer.calculate_average_word_length("hello world")
            5.0
        """
        if not text or not text.strip():
            return 0.0
            
        # Split by whitespace and keep punctuation
        words = text.split()
        
        if not words:
            return 0.0
        
        # Use a while loop to calculate total length
        total_length = 0
        i = 0
        while i < len(words):
            # Remove punctuation from each word
            clean_word = words[i].strip(string.punctuation)
            total_length += len(clean_word)
            i += 1
        
        average = total_length / len(words)
        result = round(average, 2)
        logger.debug(f"Average word length: {result}")
        
        return result
        
    def count_paragraphs(self, text: str) -> int:
        """
        Count the number of paragraphs in the text using a while loop.
        
        Paragraphs are defined by empty lines between blocks of text.
        
        Args:
            text (str): The text to analyze
            
        Returns:
            int: Number of paragraphs
            
        Examples:
            >>> analyzer = TextAnalyzer()
            >>> analyzer.count_paragraphs("Hello\\n\\nWorld")
            2
        """
        if not text or not text.strip():
            return 1
            
        # Split by double newlines (empty lines)
        paragraphs = text.split('\n\n')
        
        # Use a while loop to filter out empty paragraphs
        non_empty_paragraphs = []
        i = 0
        while i < len(paragraphs):
            if paragraphs[i].strip():
                non_empty_paragraphs.append(paragraphs[i].strip())
            i += 1
        
        count = len(non_empty_paragraphs) if non_empty_paragraphs else 1
        logger.debug(f"Number of paragraphs: {count}")
        
        return count
        
    def count_sentences(self, text: str) -> int:
        """
        Count the number of sentences in the text using a while loop.
        
        Sentences are defined by punctuation marks: ., !, ?
        
        Args:
            text (str): The text to analyze
            
        Returns:
            int: Number of sentences
            
        Examples:
            >>> analyzer = TextAnalyzer()
            >>> analyzer.count_sentences("Hello world! How are you?")
            2
        """
        if not text or not text.strip():
            return 1
            
        # Split by sentence-ending punctuation
        # Handle common abbreviations
        common_abbr = ['Mr.', 'Mrs.', 'Dr.', 'Prof.', 'Inc.', 'Co.', 'Ltd.', 'etc.']
        
        text_processed = text
        i = 0
        while i < len(common_abbr):
            text_processed = text_processed.replace(common_abbr[i], common_abbr[i].replace('.', '|||'))
            i += 1
        
        # Split by sentence boundaries
        sentences = re.split(r'[.!?]+', text_processed)
        
        # Replace back the abbreviations using a while loop
        j = 0
        while j < len(sentences):
            sentences[j] = sentences[j].replace('|||', '.')
            j += 1
        
        # Filter out empty sentences using a while loop
        non_empty_sentences = []
        k = 0
        while k < len(sentences):
            if sentences[k].strip():
                non_empty_sentences.append(sentences[k].strip())
            k += 1
        
        count = len(non_empty_sentences) if non_empty_sentences else 1
        logger.debug(f"Number of sentences: {count}")
        
        return count
        
    def get_text_statistics(self) -> Dict:
        """
        Get comprehensive statistics about the text.
        
        Returns:
            Dict: Dictionary containing various statistics
        """
        if not self.text:
            return {
                'total_words': 0,
                'unique_words': 0,
                'most_common_word': None,
                'avg_word_length': 0.0,
                'total_characters': 0,
                'total_paragraphs': 1,
                'total_sentences': 1,
                'word_frequency': []
            }
            
        # Clean text for word counting
        cleaned = re.sub(r'[^\w\s]', '', self.text)
        words = cleaned.lower().split()
        
        word_freq = self.get_word_frequency(self.text, 10)
        
        stats = {
            'total_words': len(words),
            'unique_words': len(set(words)),
            'most_common_word': self.identify_most_common_word(self.text),
            'avg_word_length': self.calculate_average_word_length(self.text),
            'total_characters': len(self.text.replace('\n', '').replace(' ', '')),
            'total_paragraphs': self.count_paragraphs(self.text),
            'total_sentences': self.count_sentences(self.text),
            'word_frequency': word_freq
        }
        
        logger.debug(f"Generated statistics: {len(stats)} metrics")
        
        return stats
