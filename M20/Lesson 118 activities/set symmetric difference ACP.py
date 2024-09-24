# Function to find symmetric difference
def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Example A: Set of colors
set1_A = {'blue', 'green'}
set2_A = {'blue', 'yellow'}
sym_diff_A = find_symmetric_difference(set1_A, set2_A)
print(f"Symmetric difference between Set1 and Set2 (Example A): {sym_diff_A}")

# Example B: Set of numbers
set1_B = {1, 2, 3, 4, 5}
set2_B = {1, 5, 6, 7, 8, 9}
sym_diff_B = find_symmetric_difference(set1_B, set2_B)
print(f"Symmetric difference between Set1 and Set2 (Example B): {sym_diff_B}")
