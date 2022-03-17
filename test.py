import struct


# Input a, b from user
a = float(input("Enter a: "))
b = float(input("Enter b: "))

# Convert a, b to bytes
a_bytes = struct.pack('>f', a)
b_bytes = struct.pack('>f', b)

# Print hex, binary, and decimal values of a, b
print("a:", a)
print("Hex:", hex(struct.unpack('>I', a_bytes)[0]))
print("Binary:", bin(struct.unpack('>I', a_bytes)[0]))
print("Decimal:", struct.unpack('>I', a_bytes)[0])
print("b:", b)
print("Hex:", hex(struct.unpack('>I', b_bytes)[0]))
print("Binary:", bin(struct.unpack('>I', b_bytes)[0]))
print("Decimal:", struct.unpack('>I', b_bytes)[0])


# Add a, b to c
c = struct.unpack('>f', a_bytes)[0] + struct.unpack('>f', b_bytes)[0]

# Print hex, binary, and decimal values of c
print("c:", c)
print("Hex:", hex(struct.unpack('>I', struct.pack('>f', c))[0]))
print("Binary:", bin(struct.unpack('>I', struct.pack('>f', c))[0]))
print("Decimal:", struct.unpack('>I', struct.pack('>f', c))[0])
