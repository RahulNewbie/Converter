from utility.constants import FileMode
from converter.converter import Converter

if __name__ == "__main__":
    # Create object for the converter class
    converter_object = Converter(
        FileMode.INPUT,
        FileMode.OUTPUT
    )
    # Run the application
    converter_object.start_processing()
