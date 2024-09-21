def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')

# Adding a newline after each binary conversion for clarity
print("Binary of 7:", end=' ')
DecimalToBinary(7)
print()  # Newline

print("Binary of 28:", end=' ')
DecimalToBinary(28)
print()  # Newline

print("Binary of 5:", end=' ')
DecimalToBinary(5)
print()  # Newline