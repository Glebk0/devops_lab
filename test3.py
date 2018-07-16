import unittest
import task3


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(task3.factorial(5), 120)

    def test_negative_error(self):
        with self.assertRaises(ValueError):
            task3.factorial(-1)


if __name__ == '__main__':
    unittest.main()