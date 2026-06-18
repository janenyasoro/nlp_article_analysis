"""
Unit tests for the FileHandler class.
"""

import unittest
import os
import tempfile
from pathlib import Path
import sys

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):
    """Test cases for FileHandler class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.file_handler = FileHandler(self.temp_dir)
        
        # Create a test file
        self.test_file = Path(self.temp_dir) / "test.txt"
        self.test_content = "This is a test file."
        self.test_file.write_text(self.test_content)
        
    def tearDown(self):
        """Clean up test files."""
        import shutil
        shutil.rmtree(self.temp_dir)
        
    def test_read_text_file(self):
        """Test reading a text file."""
        content = self.file_handler.read_text_file(str(self.test_file))
        self.assertEqual(content, self.test_content)
        
    def test_read_nonexistent_file(self):
        """Test reading a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            self.file_handler.read_text_file("nonexistent.txt")
            
    def test_write_results(self):
        """Test writing results to a file."""
        output_file = Path(self.temp_dir) / "output.txt"
        content = "Test output"
        
        self.file_handler.write_results(str(output_file), content)
        self.assertTrue(output_file.exists())
        self.assertEqual(output_file.read_text(), content)
        
    def test_get_file_info(self):
        """Test getting file information."""
        info = self.file_handler.get_file_info(str(self.test_file))
        self.assertIsNotNone(info)
        self.assertEqual(info['path'], str(self.test_file))
        self.assertFalse(info['is_empty'])
        
    def test_get_file_info_nonexistent(self):
        """Test getting info for non-existent file."""
        info = self.file_handler.get_file_info("nonexistent.txt")
        self.assertIsNone(info)


if __name__ == '__main__':
    unittest.main()