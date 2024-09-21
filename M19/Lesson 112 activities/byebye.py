valid = False

#using nested while loop

while not valid:
  try:
    n = int(input("Enter a number: "))
    
    #enter an even number
    while n%2 == 0:
      print("bye")
      valid = True

  except ValueError:
    print("Invalid")