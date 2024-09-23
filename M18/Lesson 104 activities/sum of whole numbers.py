#input an integer value
n = int(input('Enter the number whose sum you want to find: '))
sum = 0

#Iterates for n+1 time: i=1 to n+1 
for i in range(1, n+1):
    sum = sum+i
    print('\n Sum =', sum)