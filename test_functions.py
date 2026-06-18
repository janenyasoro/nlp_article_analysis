#!/usr/bin/env python3
"""
Simple test script to verify the text analysis functions.
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.text_analyzer import TextAnalyzer


def count_specific_word(text: str, search_word: str) -> int:
    """Wrapper function for counting specific words."""
    analyzer = TextAnalyzer()
    return analyzer.count_specific_word(text, search_word)


def identify_most_common_word(text: str) -> str:
    """Wrapper function for identifying the most common word."""
    analyzer = TextAnalyzer()
    return analyzer.identify_most_common_word(text)


def calculate_average_word_length(text: str) -> float:
    """Wrapper function for calculating average word length."""
    analyzer = TextAnalyzer()
    return analyzer.calculate_average_word_length(text)


def count_paragraphs(text: str) -> int:
    """Wrapper function for counting paragraphs."""
    analyzer = TextAnalyzer()
    return analyzer.count_paragraphs(text)


def count_sentences(text: str) -> int:
    """Wrapper function for counting sentences."""
    analyzer = TextAnalyzer()
    return analyzer.count_sentences(text)


def run_tests():
    """Run all test cases."""
    print("=" * 60)
    print("Running Text Analysis Function Tests")
    print("=" * 60)
    
    # Test 1: count_specific_word
    print("\n1. Testing count_specific_word:")
    test_cases = [
        ("This is a test. This is only a test.", "test", 2),
        ("apple apple banana banana banana", "banana", 3),
        ("", "test", 0),
        ("Hello world hello", "hello", 2),
        ("The quick brown fox", "the", 1),
    ]
    
    for text, word, expected in test_cases:
        result = count_specific_word(text, word)
        status = "✅ PASS" if result == expected else f"❌ FAIL (expected {expected})"
        print(f"  count_specific_word('{text[:30]}...', '{word}') = {result} {status}")
    
    # Test 2: identify_most_common_word
    print("\n2. Testing identify_most_common_word:")
    test_cases = [
        ("hello world hello world world", "world"),
        ("This is a test. This is only a test.", "test"),
        ("", None),
    ]
    
    for text, expected in test_cases:
        result = identify_most_common_word(text)
        status = "✅ PASS" if result == expected else f"❌ FAIL (expected {expected})"
        print(f"  identify_most_common_word('{text[:30]}...') = '{result}' {status}")
    
    # Test 3: calculate_average_word_length
    print("\n3. Testing calculate_average_word_length:")
    test_cases = [
        ("hello world", 5.0),
        ("the quick brown fox", 4.0),
        ("", 0.0),
    ]
    
    for text, expected in test_cases:
        result = calculate_average_word_length(text)
        status = "✅ PASS" if result == expected else f"❌ FAIL (expected {expected})"
        print(f"  calculate_average_word_length('{text[:30]}...') = {result} {status}")
    
    # Test 4: count_paragraphs
    print("\n4. Testing count_paragraphs:")
    test_cases = [
        ("First paragraph.\n\nSecond paragraph.", 2),
        ("Single paragraph.", 1),
        ("", 1),
    ]
    
    for text, expected in test_cases:
        result = count_paragraphs(text)
        status = "✅ PASS" if result == expected else f"❌ FAIL (expected {expected})"
        print(f"  count_paragraphs('{text[:30]}...') = {result} {status}")
    
    # Test 5: count_sentences
    print("\n5. Testing count_sentences:")
    test_cases = [
        ("Hello world! How are you? I'm fine.", 3),
        ("Hello world", 1),
        ("", 1),
    ]
    
    for text, expected in test_cases:
        result = count_sentences(text)
        status = "✅ PASS" if result == expected else f"❌ FAIL (expected {expected})"
        print(f"  count_sentences('{text[:30]}...') = {result} {status}")
    
    print("\n" + "=" * 60)
    print("Test Complete!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
