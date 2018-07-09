import sys


def program_exit(msg):
    print(msg)
    sys.exit(0)


INCORRECT_PYTHON_VERSION = "Script should be running on Python 3."
if sys.version_info[0] != 3:
    program_exit(INCORRECT_PYTHON_VERSION)
    
from enum import IntEnum


class ChessAddress(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8


class AddressChecker:
    EMPTY_ADDRESS_ERROR = "You should to pass an address of board cell."
    INCORRECT_ADDRESS_LENGTH_ERROR = "Address should be contained from " \
                                     "2 chars. For example A1 or G3."
    INCORRECT_FIRST_ADDRESS_CHAR = "Incorrect first address char."
    INCORRECT_SECOND_ADDRESS_CHAR = "Incorrect second address char."

    def __init__(self, terminal_args):
        self.first_address_chars = (c.name for c in ChessAddress)
        self.second_address_chars = (c.value for c in ChessAddress)
        self.address = None

        self.check_terminal_args(terminal_args)

    def __call__(self, *args, **kwargs):
        self.get_color()

    def check_terminal_args(self, args):
        if len(args) == 1:
            program_exit(self.EMPTY_ADDRESS_ERROR)
        if len(args[1]) != 2:
            program_exit(self.INCORRECT_ADDRESS_LENGTH_ERROR)
        address = args[1]
        if not self.address_char_is_correct(address[0]):
            program_exit(self.INCORRECT_FIRST_ADDRESS_CHAR)
        if not self.address_char_is_correct(address[1], True):
            program_exit(self.INCORRECT_SECOND_ADDRESS_CHAR)
        self.address = address

    def address_char_is_correct(self, _char, numeric=False):
        if numeric:
            return _char.isnumeric() and int(_char) in \
                   self.second_address_chars
        return _char.isalpha() and _char.upper() in self.first_address_chars

    def get_color(self):
        first_char = self.address[0].upper()
        first_char_to_int = ChessAddress[first_char].value
        second_char_to_int = int(self.address[1])
        if (first_char_to_int + second_char_to_int) % 2:
            print("Black")
        else:
            print("White")


if __name__ == '__main__':
    _args = sys.argv
    checker = AddressChecker(_args)
    checker()
