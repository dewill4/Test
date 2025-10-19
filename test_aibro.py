"""
Unit tests for the Aibro.ai test module.
"""

import unittest
from aibro_test import greet, add


class TestAibroModule(unittest.TestCase):
    """Test cases for the Aibro.ai test module."""
    
    def test_greet_default(self):
        """Test greeting with default name."""
        result = greet()
        self.assertEqual(result, "Hello, World!")
    
    def test_greet_with_name(self):
        """Test greeting with a custom name."""
        result = greet("Aibro")
        self.assertEqual(result, "Hello, Aibro!")
    
    def test_greet_empty_name(self):
        """Test greeting with empty name raises ValueError."""
        with self.assertRaises(ValueError):
            greet("")
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        result = add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        result = add(-5, -3)
        self.assertEqual(result, -8)
    
    def test_add_mixed_numbers(self):
        """Test adding mixed positive and negative numbers."""
        result = add(10, -5)
        self.assertEqual(result, 5)
    
    def test_add_zero(self):
        """Test adding with zero."""
        result = add(5, 0)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
