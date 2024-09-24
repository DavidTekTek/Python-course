num1 = [1, 2, 3]
num2 = [4, 5, 6]

res = map(lambda x, y: x+y, num1, num2)
print('Addition of two list')
print(list(res))

#using map
nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print('Square of numbers in list')
print(square)