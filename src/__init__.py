"""
NLP Article Analysis Package

This package provides tools for analyzing text content from news articles,
including word frequency analysis, paragraph counting, and sentence detection.
"""

from src.text_analyzer import TextAnalyzer
from src.file_handler import FileHandler
from src.utils import setup_logging, validate_text

__version__ = "1.0.0"
__all__ = ['TextAnalyzer', 'FileHandler', 'setup_logging', 'validate_text']