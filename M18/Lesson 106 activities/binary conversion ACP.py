def convert_to_binary(n):
  if n > 1:
    convert_to_binary(n//2 )
  print(n%2 , end=" " )

dec=float(input("Enter a number to find it's binary value: "))
convert_to_binary(dec)
print()

dec=float(input("Enter a number to find it's binary value: "))

def convert_to_binary(n):
  if n > 1:
    convert_to_binary(n//2 )
  print(n%2 , end=" " )


convert_to_binary(dec)
print()