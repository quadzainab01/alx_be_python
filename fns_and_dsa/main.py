from arithmetic_operations import perform_operation  # Import the perform_operation function from arithmetic_operations.py

def main():
    print("Arithmetic Operations")  # Display a title message

    # Prompt the user to enter the first number and convert it to float
    num1 = float(input("Enter the first number: "))

    # Prompt the user to enter the second number and convert it to float
    num2 = float(input("Enter the second number: "))

    # Prompt the user to enter the operation (add, subtract, multiply, divide)
    # Use strip() to remove any extra spaces and lower() to make the input lowercase for easier comparison
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Call the perform_operation function with the inputs and store the result
    result = perform_operation(num1, num2, operation)

    # Print the result to the user
    print(f"Result: {result}")

# This ensures that main() runs only when this script is executed directly,
# and not when imported as a module in another script
if __name__ == "__main__":
    main()
