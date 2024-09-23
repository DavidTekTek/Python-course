# take marks as input from user
print('Enter marks obtained in 4 subjects: ')
math = int(input('Maths: '))
eng = int(input('English: '))
sci = int(input('Science: '))
yor = int(input('Yoruba: '))

# calculate percentage
sum = math + eng + sci + yor
print('Sum of Maths, English, Science, and Yoruba')

perc = (sum/400) * 100

print(end= "Percentage mark = ")
print(perc)