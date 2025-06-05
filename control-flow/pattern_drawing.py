
# Drawing Patterns with While and For Loops

# Prompt the user for pattern size
pattern_size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for the rows
while row < pattern_size:

# Use a for loop for the columns (stars in a row)
    for col in range(pattern_size):

	print("*", end="")

    print()  # Move to the next line after each row

    row += 1  # Go to the next row
