# test_pixelblock.py
"""
Tests for PixelBlock module.
"""

import unittest
from pixelblock import PixelBlock

class TestPixelBlock(unittest.TestCase):
    """Test cases for PixelBlock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PixelBlock()
        self.assertIsInstance(instance, PixelBlock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PixelBlock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
