import unittest
from fizzbuzz import fizzbuzz


class TestFizzbuzz(unittest.TestCase):

    def test_one(self):
        self.assertEqual(fizzbuzz.process(1), str(1))

    def test_fizz(self):
        self.assertEqual(fizzbuzz.process(3), 'Fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzz.process(5), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.process(15), 'FizzBuzz')


class TestInput(unittest.TestCase):

    def test_valid_input(self):
        self.assertTrue(fizzbuzz.is_valid_countable_number(1))
        self.assertFalse(fizzbuzz.is_valid_countable_number(0))
        self.assertFalse(fizzbuzz.is_valid_countable_number(-1))


if __name__ == '__main__':
    unittest.main()
