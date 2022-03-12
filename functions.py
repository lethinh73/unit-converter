import struct


# Add two binary numbers
def add_binary(num1, num2):
    return bin(int(num1, 2) + int(num2, 2)).replace("0b", "")


# Subtract two binary numbers
def sub_binary(num1, num2):
    return bin(int(num1, 2) - int(num2, 2)).replace("0b", "")


# Multiply two binary numbers
def mul_binary(num1, num2):
    return bin(int(num1, 2) * int(num2, 2)).replace("0b", "")


# AND two binary number
def and_binary(num1, num2):
    return bin(int(num1, 2) & int(num2, 2)).replace("0b", "")


# OR two binary number
def or_binary(num1, num2):
    return bin(int(num1, 2) | int(num2, 2)).replace("0b", "")


# NOT two binary number
def not_binary(num1):
    a = int(num1, 2)
    a = ~a
    return bin(a).replace("0b", "")


# XOR two binary number
def xor_binary(num1, num2):
    return bin(int(num1, 2) ^ int(num2, 2)).replace("0b", "")


# NOR two binary numbers
def nor_binary(num1, num2):
    return bin(int(num1, 2) & int(num2, 2)).replace("0b", "")


# Float to SEM
def float_to_bin(num):
    byteFormat = struct.pack('!f', num)
    uIntegerFormat = struct.unpack('!I', byteFormat)
    return bin(uIntegerFormat[0])[2:].zfill(32)


# SEM to float
def bin_to_float(binary):
    byteFormat = struct.pack('!I', int(binary, 2))
    return struct.unpack('!f', byteFormat)[0]
