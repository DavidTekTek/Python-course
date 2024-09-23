def check_fire():
    print('Fire Risk Assessment')
    
temp = float(input('Enter the temperature in Celsius: '))
smoke_level = input('Is there smoke? (yes/no): ')
flames = input('Are there visible flames? (yes/no): ')

if temp > 50 or smoke_level.lower() == "yes" or flames.lower() == "yes":
    print("Call the fire brigade!")
else:
    print("No need to call the fire brigade.")
    
check_fire()