def perform_operation(num1, num2, operation):
    # Check if the operation is addition
    if operation == "add":
        return num1 + num2  # Return the sum of num1 and num2

    # Check if the operation is subtraction
    elif operation == "subtract":
        return num1 - num2  # Return the difference (num1 minus num2)

    # Check if the operation is multiplication
    elif operation == "multiply":
        return num1 * num2  # Return the product of num1 and num2

    # Check if the operation is division
    elif operation == "divide":
        # Handle division by zero case
        if num2 == 0:
            return "Error: Cannot divide by zero."  # Return an error message for division by zero
        else:
            return num1 / num2  # Return the quotient of num1 divided by num2

    # Handle invalid operation inputs
    else:
        return "Invalid operation"  # Return a message for unsupported operations
