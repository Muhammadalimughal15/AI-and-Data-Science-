class StringProcessor:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string(self):
        print(self.input_string.upper())


def test_string_processor():
    processor = StringProcessor()
    processor.get_string()
    processor.print_string()


test_string_processor()