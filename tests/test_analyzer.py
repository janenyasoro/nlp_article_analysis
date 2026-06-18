"""
Unit tests for the TextAnalyzer class.
"""

import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.text_analyzer import TextAnalyzer


class TestTextAnalyzer(unittest.TestCase):
    """Test cases for TextAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = TextAnalyzer()
        
        # Sample text for testing
        self.sample_text = """
        ACME Inc. has launched a revolutionary apple pie machine.
        The Apple Pie Master uses advanced artificial intelligence.
        It can peel apples and roll out pie crusts.
        The machine is user-friendly and environmentally friendly.
        """
        self.analyzer.set_text(self.sample_text)
        
    def test_count_specific_word(self):
        """Test counting specific words."""
        # Case insensitive matching
        count = self.analyzer.count_specific_word(self.sample_text, "apple")
        self.assertEqual(count, 2)  # "apple" appears twice
        
        # Word with different case
        count = self.analyzer.count_specific_word(self.sample_text, "ACME")
        self.assertEqual(count, 1)
        
        # Word not found
        count = self.analyzer.count_specific_word(self.sample_text, "banana")
        self.assertEqual(count, 0)
        
        # Edge cases
        self.assertEqual(self.analyzer.count_specific_word("", "test"), 0)
        self.assertEqual(self.analyzer.count_specific_word("Hello", ""), 0)
        
    def test_identify_most_common_word(self):
        """Test identifying the most common word."""
        text = "hello world hello world world"
        most_common = self.analyzer.identify_most_common_word(text)
        self.assertEqual(most_common, "world")
        
        # Test with punctuation
        text = "Hello, world! Hello, world! Hello!"
        most_common = self.analyzer.identify_most_common_word(text)
        self.assertEqual(most_common, "hello")
        
        # Edge cases
        self.assertIsNone(self.analyzer.identify_most_common_word(""))
        self.assertIsNone(self.analyzer.identify_most_common_word("   "))
        
    def test_calculate_average_word_length(self):
        """Test calculating average word length."""
        text = "hello world"
        avg = self.analyzer.calculate_average_word_length(text)
        self.assertEqual(avg, 5.0)
        
        # Updated test - "the quick brown fox"
        # Words: the(3), quick(5), brown(5), fox(3)
        # Average = (3+5+5+3)/4 = 16/4 = 4.0
        text = "the quick brown fox"
        avg = self.analyzer.calculate_average_word_length(text)
        self.assertEqual(avg, 4.0)
        
        # Test with punctuation
        text = "Hello, world! How are you?"
        avg = self.analyzer.calculate_average_word_length(text)
        # Words: Hello(5), world(5), How(3), are(3), you(3)
        # Average = (5+5+3+3+3)/5 = 19/5 = 3.8
        self.assertEqual(avg, 3.8)
        
        # Edge cases
        self.assertEqual(self.analyzer.calculate_average_word_length(""), 0.0)
        self.assertEqual(self.analyzer.calculate_average_word_length("   "), 0.0)
        
    def test_count_paragraphs(self):
        """Test counting paragraphs."""
        text = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        count = self.analyzer.count_paragraphs(text)
        self.assertEqual(count, 3)
        
        # Single paragraph
        text = "This is a single paragraph."
        count = self.analyzer.count_paragraphs(text)
        self.assertEqual(count, 1)
        
        # Edge cases
        self.assertEqual(self.analyzer.count_paragraphs(""), 1)
        self.assertEqual(self.analyzer.count_paragraphs("   "), 1)
        
    def test_count_sentences(self):
        """Test counting sentences."""
        text = "Hello world! How are you? I'm fine."
        count = self.analyzer.count_sentences(text)
        self.assertEqual(count, 3)
        
        text = "Dr. Smith said hello."
        count = self.analyzer.count_sentences(text)
        self.assertEqual(count, 1)  # Should handle Dr. abbreviation
        
        # Edge cases
        self.assertEqual(self.analyzer.count_sentences(""), 1)
        self.assertEqual(self.analyzer.count_sentences("   "), 1)
        
    def test_get_text_statistics(self):
        """Test getting comprehensive statistics."""
        stats = self.analyzer.get_text_statistics()
        self.assertIsInstance(stats, dict)
        self.assertIn('total_words', stats)
        self.assertIn('unique_words', stats)
        self.assertIn('most_common_word', stats)
        self.assertIn('avg_word_length', stats)
        
        # Test with empty text
        self.analyzer.set_text("")
        stats = self.analyzer.get_text_statistics()
        self.assertEqual(stats['total_words'], 0)
        self.assertEqual(stats['total_paragraphs'], 1)
        
    def test_get_word_frequency(self):
        """Test getting word frequency."""
        text = "hello world hello world world"
        freq = self.analyzer.get_word_frequency(text, 2)
        self.assertEqual(freq[0], ("world", 3))
        self.assertEqual(freq[1], ("hello", 2))


if __name__ == '__main__':
    unittest.main()
