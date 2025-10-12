import unittest
import os
from main import is_prime, fibonacci, get_file_content, sum_of_many_numbers

class TestMain(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(10), 55)

    def test_get_file_content(self):
        # Create a dummy file to test with
        with open("test_file.txt", "w") as f:
            f.write("Hello, world!")

        self.assertEqual(get_file_content("test_file.txt"), "Hello, world!")
        self.assertEqual(get_file_content("non_existent_file.txt"), "Error: File not found.")

        # Clean up the dummy file
        os.remove("test_file.txt")

    def test_sum_of_many_numbers(self):
        self.assertEqual(sum_of_many_numbers(1, 2, 3), 6)
        self.assertEqual(sum_of_many_numbers(10, 20, 30, 40, 50), 150)
        self.assertEqual(sum_of_many_numbers(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()