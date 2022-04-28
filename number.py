import struct


class Number:
    # Constructor, convert number to float format
    def __init__(self, num=0):
        self.num = struct.pack('>f', num)

    # Set number (from decimal)
    def set_from_float(self, num):
        print('Import number from float: ', num)
        self.num = struct.pack('>f', num)

    # Set number (from binary string)
    def set_from_bin(self, num):
        print('Import number from binary: ', num)
        self.num = struct.pack('>I', int(num, 2))

    # Set number (from hex string)
    def set_from_hex(self, num):
        print('Import number from hex: ', num)
        self.num = struct.pack('>I', int(num, 16))

    # Get binary string
    def get_bin(self):
        result = bin(struct.unpack('>I', self.num)[0]).replace('0b', '').zfill(32)
        print('Export binary: ', result)
        return result

    # Get float value
    def get_float(self):
        result = struct.unpack('>f', self.num)[0]
        print('Export float: ', result)
        return result

    # Get hex value
    def get_hex(self):
        result = hex(struct.unpack('>I', self.num)[0]).replace('0x', '').zfill(8)
        print('Export hex: ', result)
        return result

    # ADD operation
    def __add__(self, other):
        print('Addition between: ', self.get_float(), ' and ', other.get_float())
        return Number(self.get_float() + other.get_float())

    # SUB operation
    def __sub__(self, other):
        print('Subtraction between: ', self.get_float(), ' and ', other.get_float())
        return Number(self.get_float() - other.get_float())

    # MUL operation
    def __mul__(self, other):
        print('Multiplication between: ', self.get_float(), ' and ', other.get_float())
        return Number(self.get_float() * other.get_float())

    # DIV operation
    def __truediv__(self, other):
        print('Division between: ', self.get_float(), ' and ', other.get_float())
        return Number(self.get_float() / other.get_float())

    # AND operation
    def __and__(self, other):
        print('AND between: ', self.get_float(), ' and ', other.get_float())
        return Number(int(self.get_float()) & int(other.get_float()))

    # OR operation
    def __or__(self, other):
        print('OR between: ', self.get_float(), ' and ', other.get_float())
        return Number(int(self.get_float()) | int(other.get_float()))

    # XOR operation
    def __xor__(self, other):
        print('XOR between: ', self.get_float(), ' and ', other.get_float())
        return Number(int(self.get_float()) ^ int(other.get_float()))

    # NOT operation
    def __invert__(self):
        print('NOT operation for: ', self.get_float())
        return Number(~int(self.get_float()))

    # LSHIFT operation
    def __lshift__(self, other):
        print('LSHIFT between: ', self.get_float(), ' and ', other.get_float())
        return Number(int(self.get_float()) << int(other.get_float()))

    # RSHIFT operation
    def __rshift__(self, other):
        print('RSHIFT between: ', self.get_float(), ' and ', other.get_float())
        return Number(int(self.get_float()) >> int(other.get_float()))

        