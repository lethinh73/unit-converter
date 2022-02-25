def float_to_bin(floating):
    result = []

    while True:

        floating *= 2

        if floating >= 1:
            result.append(1)
            floating -= 1
        else:
            result.append(0)

        if result.__len__() == 23 or floating == 0:
            break

    return result


def whole_to_bin(number):
    reversed_result = []

    while True:

        reversed_result.append(number % 2)
        number = int(number / 2)

        if number <= 0:
            break

    return reversed_result[::-1]


print(whole_to_bin(263))
print(float_to_bin(0.3))
