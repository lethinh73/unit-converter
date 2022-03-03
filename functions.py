# Convert fraction part to binary
def fraction_to_bin(fraction):
    result = ""

    while True:
        fraction *= 2

        if fraction >= 1:
            result += "1"
            fraction -= 1
        else:
            result += "0"

        if result.__len__() >= 23 or fraction == 0:
            break

    return result


# Convert integer part to binary
def whole_to_bin(number):
    return bin(number)
