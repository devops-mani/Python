def get_integer_input(prompt):
    """ Helper function to get integer input from the user """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

# Get the size of the array
N = get_integer_input("Enter the size of the array: ")

# Get the elements of the array
array = []
for i in range(N):
    array.append(get_integer_input(f"Enter integer number {i + 1}: "))

# Get the number of rotations
d = get_integer_input("Enter the number of times you want to rotate the array: ")

# Normalize d to be within the range of 0 to N-1
d = d % N

# Rotate the array to the left by d positions
rotated_array = array[d:] + array[:d]

# Print the result
print("Rotated Array:", rotated_array)


###
Usage Example:
text
Copy code
Enter the size of the array: 5
Enter integer number 1: 10
Enter integer number 2: 20
Enter integer number 3: 30
Enter integer number 4: 40
Enter integer number 5: 50
Enter the number of times you want to rotate the array: 2
Rotated Array: [30, 40, 50, 10, 20]
###
