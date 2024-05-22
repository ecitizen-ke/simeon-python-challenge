import unittest
from palindrome_checker import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Racecar"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("Hello, World!"))
        self.assertFalse(is_palindrome("Python"))
        self.assertFalse(is_palindrome("GitHub"))

if __name__ == '__main__':
    unittest.main()
