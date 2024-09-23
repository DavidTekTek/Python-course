num = int(input("Enter any number\n"))

count = 0

while num != 0:
  count += 1
  num = num//10

print(count)