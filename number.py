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
        if('-' in num):
            num = num.replace('-', '')
            sign = -1

        if('.' in num):
            dec_bin = num.split('.')[0]
            fl_bin = num.split('.')[1]

            print('dec_bin:', dec_bin)
            print('fl_bin:', fl_bin)

            dec = 0
            fl = 0

            count = len(dec_bin) - 1

            for i in range(len(dec_bin)):
                dec += int(dec_bin[i]) * (2 ** count)
                count -= 1

            count = -1

            for i in range(len(fl_bin)):
                fl += int(fl_bin[i]) * (2 ** count)
                count -= 1

            if(sign == -1):
                self.num = struct.pack('>f', -(dec + fl))
            else:
                self.num = struct.pack('>f', dec + fl)
        else:
            dec = 0

            count = len(num) - 1

            for i in range(len(num)):
                dec += int(num[i]) * (2 ** count)
                count -= 1

            if(sign == -1):
                self.num = struct.pack('>f', -dec)
            else:
                self.num = struct.pack('>f', dec)

    # Return SEM value
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

        if(num < 0):
            sign = -1
            num = abs(num)
        else:
            sign = 1

        if('.' in str(num)):
            dec = int(str(num).split('.')[0])
            fl = float('0.' + str(num).split('.')[1])

            dec_bin = bin(dec).replace('0b', '')
            fl_bin = ''

            while(len(fl_bin) < 32 and fl != 1 and fl != 0):
                fl *= 2
                if(fl > 1):
                    fl_bin += '1'
                    fl -= 1
                else:
                    fl_bin += '0'

            if(fl == 0):
                fl_bin += '0'

            if(sign == -1):
                return '-' + dec_bin + '.' + fl_bin
            return dec_bin + '.' + fl_bin

        else:
            return bin(num)
