"""
File handler module for reading and writing text files.
"""

import os
import logging
from pathlib import Path
from typing import Optional, List
from datetime import datetime

logger = logging.getLogger(__name__)


class FileHandler:
    """
    Handles file operations for the text analysis project.
    
    This class provides methods for reading text files, writing results,
    and managing file paths.
    """
    
    def __init__(self, base_dir: Optional[str] = None):
        """
        Initialize the FileHandler with a base directory.
        
        Args:
            base_dir (str, optional): Base directory path. Defaults to project root.
        """
        if base_dir:
            self.base_dir = Path(base_dir)
        else:
            self.base_dir = Path(__file__).parent.parent
            
        logger.debug(f"FileHandler initialized with base_dir: {self.base_dir}")
        
    def read_text_file(self, file_path: str) -> str:
        """
        Read the contents of a text file.
        
        Args:
            file_path (str): Path to the text file (absolute or relative)
            
        Returns:
            str: Content of the file
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            IOError: If there's an error reading the file
            ValueError: If the file is empty
        """
        try:
            # Handle relative paths
            if not os.path.isabs(file_path):
                file_path = self.base_dir / file_path
                
            logger.info(f"Reading file: {file_path}")
            
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
                
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
            if not content or not content.strip():
                raise ValueError(f"File {file_path} is empty")
                
            logger.info(f"Successfully read {len(content)} characters")
            return content
            
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except IOError as e:
            logger.error(f"Error reading file {file_path}: {str(e)}")
            raise
        except ValueError as e:
            logger.error(str(e))
            raise
            
    def write_results(self, file_path: str, content: str) -> None:
        """
        Write analysis results to a file.
        
        Args:
            file_path (str): Path to the output file
            content (str): Content to write
            
        Raises:
            IOError: If there's an error writing to the file
        """
        try:
            # Handle relative paths
            if not os.path.isabs(file_path):
                file_path = self.base_dir / file_path
                
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            logger.info(f"Writing results to: {file_path}")
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
                
            logger.info(f"Successfully wrote {len(content)} characters")
            
        except IOError as e:
            logger.error(f"Error writing to file {file_path}: {str(e)}")
            raise
            
    def read_multiple_files(self, file_pattern: str) -> List[str]:
        """
        Read multiple files matching a pattern.
        
        Args:
            file_pattern (str): Pattern to match files
            
        Returns:
            List[str]: List of file contents
        """
        from glob import glob
        
        files = glob(str(self.base_dir / file_pattern))
        contents = []
        
        for file_path in files:
            try:
                content = self.read_text_file(file_path)
                contents.append(content)
            except Exception as e:
                logger.warning(f"Could not read {file_path}: {str(e)}")
                
        return contents
        
    def get_file_info(self, file_path: str) -> dict:
        """
        Get information about a file.
        
        Args:
            file_path (str): Path to the file
            
        Returns:
            dict: File information including size, modification time, etc.
        """
        if not os.path.isabs(file_path):
            file_path = self.base_dir / file_path
            
        if not os.path.exists(file_path):
            return None
            
        stat = os.stat(file_path)
        
        return {
            'path': str(file_path),
            'size_bytes': stat.st_size,
            'modified': datetime.fromtimestamp(stat.st_mtime),
            'created': datetime.fromtimestamp(stat.st_ctime),
            'is_empty': stat.st_size == 0
        }