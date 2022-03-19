import struct


class Number:
    # Constructor
    def __init__(self, num=0):
        self.num = struct.pack('>f', num)

    # Set number (from float or decimal)
    def set_from_float(self, num):
        self.num = struct.pack('>f', num)

    # Set number (from SEM string)
    def set_from_sem(self, num):
        self.num = struct.pack('>I', int(num, 2))

    # Set number (from hex string)
    def set_from_hex(self, num):
        self.num = struct.pack('>I', int(num, 16))

    # Set number (from binary string)
    def set_from_binary(self, num):
        if('.' in num):
            dec_str = num.split('.')[0]
            fl_str = num.split('.')[1]

            dec = int(dec_str, 2)
            fl = 0

            for i in range(len(fl_str)):
                fl += int(fl_str[i]) * 2 ** (-i - 1)

            self.num = struct.pack('>f', dec + fl)
        else:
            if(num[0] == '-'):
                self.num = struct.pack('>f', -int(num[1:], 2))
            else:
                self.num = struct.pack('>f', int(num, 2))

    def get_sem(self):
        return bin(struct.unpack('>I', self.num)[0]).replace('0b', '').zfill(32)

    # Return float value
    def get_float(self):
        return struct.unpack('>f', self.num)[0]

    # Return hex value
    def get_hex(self):
        return hex(struct.unpack('>I', self.num)[0]).replace('0x', '').zfill(8)

    # Return binary value
    def get_binary(self):
        num = struct.unpack('>f', self.num)[0]

        if(abs(num) < 0.00001):
            return '0'

        if('.' in str(num)):
            dec = int(str(num).split('.')[0])
            fl = float('0.' + str(num).split('.')[1])
            fl_str = ''

            if(abs(num) < 1):
                if(num < 0):
                    dec_str = '-0'
                else:
                    dec_str = '0'
            else:
                dec_str = bin(dec).replace('0b', '')

            while(len(fl_str) < 32 and fl != 1 and fl != 0):
                fl *= 2
                if(fl >= 1):
                    fl_str += '1'
                    fl -= 1
                else:
                    fl_str += '0'

            if(fl_str == ''):
                return dec_str
            else:
                return (dec_str + '.' + fl_str).rstrip('0')
        else:
            return bin(num).replace('0b', '')

    # ADD operation
    def __add__(self, other):
        return Number(self.get_float() + other.get_float())

    # SUB operation
    def __sub__(self, other):
        return Number(self.get_float() - other.get_float())

    # MUL operation
    def __mul__(self, other):
        return Number(self.get_float() * other.get_float())

    # DIV operation
    def __truediv__(self, other):
        return Number(self.get_float() / other.get_float())

    # AND operation
    def __and__(self, other):
        return Number(int(self.get_float()) & int(other.get_float()))

    # OR operation
    def __or__(self, other):
        return Number(int(self.get_float()) | int(other.get_float()))

    # XOR operation
    def __xor__(self, other):
        return Number(int(self.get_float()) ^ int(other.get_float()))

    # NOT operation
    def __invert__(self):
        return Number(~int(self.get_float()))

    # LSHIFT operation
    def __lshift__(self, other):
        return Number(int(self.get_float()) << int(other.get_float()))

    # RSHIFT operation
    def __rshift__(self, other):
        return Number(int(self.get_float()) >> int(other.get_float()))


# Testing Number class
if __name__ == '__main__':
    n = Number()
    n.set_from_float(0.0001)
    print('n: ', n.get_float())
    print('binary: ', n.get_binary())
