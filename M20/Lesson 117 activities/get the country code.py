country_code = {'Nigeria' : '10011',
                'Australia' : '0025',
                'Nepal' : '00977'}
 
# search dictionary for country code of Nigeria
print("Country code for Nigeria -")
print(country_code.get('Nigeria', 'Not Found'))
 
# search dictionary for country code of Ethiopia
print("Country code for Ethiopia -")
print(country_code.get('Ethiopia', 'Not Found'))