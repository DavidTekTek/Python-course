# Function to find square values, then separate odd and even squares
def square_odd_even(begin, end):
    # List to store square values
    square_values = [num ** 2 for num in range(begin, end + 1)]
    
    # Separate odd and even square values
    odd_squares = [sq for sq in square_values if sq % 2 != 0]
    even_squares = [sq for sq in square_values if sq % 2 == 0]
    
    # Print results
    print("Odd square values:", odd_squares)
    print("Even square values:", even_squares)

# Input from user for the range
begin_range = int(input("Enter the beginning of the range: "))
end_range = int(input("Enter the end of the range: "))

# Call the function
square_odd_even(begin_range, end_range)
