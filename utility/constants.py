import os

# Global variable section
STANDARD_ROMAN_TO_ARABIC = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Maximum arabic number to convert to to roman
MAX_NUM_TO_CONVERT = 3999


class FileMode:
    INPUT = str(os.getcwd()) + "/input_text.txt"
    OUTPUT = str(os.getcwd()) + "/output_text.txt"
