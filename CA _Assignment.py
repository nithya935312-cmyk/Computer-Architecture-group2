
# COMPUTER ARCHITECTURE - PROBLEM SOLVING I
# Q1: Signed Binary Arithmetic
# Q2: Rotate Operations

def to_8bit(n):
    return format(n & 255, '08b')


print("===== Q1: SIGNED BINARY ARITHMETIC =====")

# (a) 34 + (+27)
a = 34
b = 27
result = a + b

print("\n(a) 34 + (+27)")
print("First operand :", to_8bit(a))
print("Second operand:", to_8bit(b))
print("Binary result :", to_8bit(result))
print("Decimal result:", result)
print("Overflow:", "Yes" if result > 127 or result < -128 else "No")


# (b) (-34) - (-27)
a = -34
b = -27
result = a - b

print("\n(b) (-34) - (-27)")
print("First operand :", to_8bit(a))
print("Second operand:", to_8bit(b))
print("Binary result :", to_8bit(result))
print("Decimal result:", result)
print("Overflow:", "Yes" if result > 127 or result < -128 else "No")


print("\n===== Q2: ROTATE OPERATIONS =====")

# (a) Rotate Left Without Carry (ROL)
num = "10110110"

print("\n(a) ROL by 2 positions")
print("Original:", num)

for i in range(2):
    num = num[1:] + num[0]
    print("After rotation", i + 1, ":", num)

print("Final result:", num)


# (b) Rotate Left Through Carry (RCL)
num = "10110110"
carry = 0

print("\n(b) RCL by 2 positions")
print("Original:", num)
print("Initial carry:", carry)

for i in range(2):
    new_carry = int(num[0])
    num = num[1:] + str(carry)
    carry = new_carry
    print("After rotation", i + 1, ":", num,
          "| Carry:", carry)

print("Final result:", num)
print("Final carry:", carry)
