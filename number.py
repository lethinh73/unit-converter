import struct


class Number:
    # Constructor
    def __init__(self, num=0.0):
        self.num = num

    # Set number
    def set(self, num):
        self.num = num

    # Set from sem
    def set_from_sem(self, sem):
        self.num = self.sem_to_float(sem)

    # Set from binary
    def set_from_bin(self, bin):
        self.num = int(bin, 2)

    # Set from hex
    def set_from_hex(self, hex):
        self.num = float(hex, 16)

    # Add operation
    def __add__(self, other):
        return Number(self.num + other.num)

    # Subtract operation
    def __sub__(self, other):
        return Number(self.num - other.num)

    # Multiply operation
    def __mul__(self, other):
        return Number(self.num * other.num)

    # Divide operation
    def __truediv__(self, other):
        return Number(self.num / other.num)

    # Or operation
    def __or__(self, other):
        return Number(int(self.num) | int(other.num))

    # And operation
    def __and__(self, other):
        return Number(int(self.num) & int(other.num))

    # Xor operation
    def __xor__(self, other):
        return Number(int(self.num) ^ int(other.num))

    # Shift left operation
    def __lshift__(self, other):
        return Number(int(self.num) << int(other.num))

    # Shift right operation
    def __rshift__(self, other):
        return Number(int(self.num) >> int(other.num))

    # Return string representation of number
    def __str__(self):
        return str(self.num)

    # Return number
    def value(self):
        return self.num

    # Return sem value
    def sem(self):
        return self.float_to_sem(self.num)

    # Float to SEM
    def float_to_sem(self, float):
        memory_format = struct.pack('!f', float)
        uInt_format = struct.unpack('!I', memory_format)[0]
        return bin(uInt_format)[2:].zfill(32)

    # SEM to float
    def sem_to_float(self, sem):
        uInt_format = struct.pack('!I', int(sem, 2))
        return struct.unpack('!f', uInt_format)[0]
