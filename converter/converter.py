from utility.constants import MAX_NUM_TO_CONVERT, \
    STANDARD_ROMAN_TO_ARABIC
from reader.reader import Reader
from writer.writer import Writer


class Converter:
    """
    Class Converter to convert Roman to arabic number
    """
    def __init__(self, input_file_path, output_file_path):
        self.max_num = MAX_NUM_TO_CONVERT
        self.converter_list = STANDARD_ROMAN_TO_ARABIC
        self.reader = Reader(input_file_path)
        self.writer = Writer(output_file_path)

    def if_roman(self, roman_number):
        """
        Check if the incoming roman number is valid
        """
        if isinstance(roman_number, int):
            return False
        elif not roman_number[0] in self.converter_list.keys():
            return False
        else:
            return True

    def roman_to_arabic(self, roman_number):
        """
        Method to convert the Roman number to arabic number
        """
        int_val = 0
        # Check if it is a valid roman number
        if not self.if_roman(roman_number):
            raise ValueError('Input number {} is not a valid roman numeric'.format(roman_number))
        # Convert the the valid roman numeric to arabic number
        for iteration in range(len(roman_number)):
            if iteration > 0 and self.converter_list[roman_number[iteration]] > \
                    self.converter_list[roman_number[iteration - 1]]:
                int_val += self.converter_list[roman_number[iteration]] - \
                            2 * self.converter_list[roman_number[iteration - 1]]
            else:
                int_val += self.converter_list[roman_number[iteration]]

        return int_val

    def start_processing(self):
        """
        Responsible to start reading the input file, convert
        the roman numeric to arabic and save it into output file
        """
        for roman_number in self.reader.read_file_by_line():
            arabic_numeric = self.roman_to_arabic(roman_number)
            self.writer.write_file(arabic_numeric)
        self.writer.close_file()







