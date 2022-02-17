def BinarytoDecimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i])*(2**(len(binary)-i-1))
    return decimal

def DecimaltoBinary(decimal):
    binary = ''
    while decimal > 0:
        binary = str(decimal%2) + binary
        decimal = decimal//2
    return int(binary)