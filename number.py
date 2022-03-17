import struct


class Number(object):
    # Constructor
    def __init__(self, num = 0):
        self.num = num
    
    # Return string representation of number
    def __str__(self):
        return str(self.num)

    # Return number
    def value(self):
        return self.num

    # Return SEM
    def float_to_sem(float):
        memory_format = struct.pack('!f', float)
        uInt_format = struct.unpack('!I', memory_format)[0]
        return bin(uInt_format)[2:].zfill(32)

    # SEM to float
    def sem_to_float(sem):
        uInt_format = struct.pack('!I', int(sem, 2))
        return struct.unpack('!f', uInt_format)[0]

print(Number.sem_to_float('01000001001000000000000000000000'))
print(Number.float_to_sem(10.0))