# Import the necessary classes from the datetime module
from datetime import datetime, timedelta

# Function to display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date}")

# Function to calculate and display a future date
def calculate_future_date():
    try:
        # Prompt the user to enter number of days to add
        days = int(input("Enter the number of days to add to the current date: "))
        # Calculate the future date by adding the number of days to the current date
        future_date = datetime.now() + timedelta(days=days)
        # Format and print the future date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        # Handle non-integer inputs
        print("Please enter a valid integer.")

# Call the functions to run the script
display_current_datetime()
calculate_future_date()
