#using a try & except
try : 
  num = int(input("Enter your number : "))
  print('The number entered is', num)

  #using ValueError
except ValueError as ex:
  print("Exception: ",ex)