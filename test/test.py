import unittest
from converter.converter import Converter
from utility.constants import FileMode


class ConverterTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = Converter(FileMode.INPUT, FileMode.OUTPUT)

    def test_invalid_type_input(self):
        self.assertRaises(ValueError, self.object.roman_to_arabic, "Roman")

    def test_input_zero(self):
        self.assertRaises(ValueError, self.object.roman_to_arabic, 0)

    def test_input_valid_roman1(self):
        self.assertEqual(127, self.object.roman_to_arabic("CXXVII"))

    def test_input_max_limit_roman(self):
        self.assertEqual(3999, self.object.roman_to_arabic("MMMCMXCIX"))

    def test_input_valid_roman2(self):
        self.assertEqual(37, self.object.roman_to_arabic("XXXVII"))


if __name__ == "__main__":
    unittest.main()
