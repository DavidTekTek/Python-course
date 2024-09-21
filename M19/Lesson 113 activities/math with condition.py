#importing math module
import math  

x = float('nan')

#to check whether the given value is number or not
if math.isnan(x): 
    print('It is not a number')
x = float('inf')
y = 45

#to check whether the given number is infinite or not
if math.isinf(x): 
    print('It is Infinity')

#x is not a finite number
print(math.isfinite(x)) 

#y is a finite number
print(math.isfinite(y)) 
print(math.isnan(y))