
class Writer:
    """
    Writer class to write the data into output file
    """
    def __init__(self, filename):
        self.filename = filename
        self.file = self.create_file()

    def create_file(self):
        """
        Create the out file
        """
        try:
            file = open(self.filename, 'a+')
            return file
        except (FileNotFoundError, Exception) as error:
            print(error)

    def write_file(self, data):
        """
        Write the data into file
        """
        try:
            self.file.write("{}\n".format(data))
        except (FileNotFoundError, Exception) as error:
            print(error)

    def close_file(self):
        """
        Close the file
        """
        try:
            self.file.close()
        except (FileNotFoundError, Exception) as error:
            print(error)

