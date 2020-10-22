
class Reader:
    """
    Class Reader to read the input file
    """
    def __init__(self, filename):
        self.file = filename

    def read_file_by_line(self):
        """
        Read the input file and return single line using generator
        """
        try:
            with open(self.file) as input_file:
                for line in input_file:
                    # Generator to send single line
                    yield line.rstrip()
        except (Exception, OSError) as error:
            print(error)
