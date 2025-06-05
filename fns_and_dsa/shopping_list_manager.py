def display_menu():
    # Function to display the main menu options to the user
    print("\nShopping List Manager")  # Print a blank line and the program title
    print("1. Add Item")             # Option 1: Add an item
    print("2. Remove Item")          # Option 2: Remove an item
    print("3. View List")            # Option 3: View the current shopping list
    print("4. Exit")                 # Option 4: Exit the program

def main():
    # Main function containing the program logic
    shopping_list = []  # Initialize an empty list to store shopping items

    while True:  # Start an infinite loop to keep the program running until user exits
        display_menu()  # Show menu options
        choice = input("Enter your choice: ").strip()  # Get user input and strip whitespace

        if choice == '1':
            # User chose to add an item
            item = input("Enter the item to add: ").strip()  # Prompt for the item name
            shopping_list.append(item)  # Add the item to the shopping list
            print(f'"{item}" has been added to your shopping list.')  # Confirm addition

        elif choice == '2':
            # User chose to remove an item
            item = input("Enter the item to remove: ").strip()  # Prompt for the item to remove
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item if it exists in the list
                print(f'"{item}" has been removed from your shopping list.')  # Confirm removal
            else:
                # Item not found in the list
                print(f'"{item}" is not in your shopping list.')  # Inform user item not found

        elif choice == '3':
            # User chose to view the shopping list
            if shopping_list:
                print("Your shopping list:")  # Print heading
                # Enumerate the list starting from 1 to number the items
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")  # Print each item with its number
            else:
                # Shopping list is empty
                print("Your shopping list is empty.")  # Inform user

        elif choice == '4':
            # User chose to exit the program
            print("Goodbye!")  # Farewell message
            break  # Exit the while loop, ending the program

        else:
            # User entered an invalid menu choice
            print("Invalid choice. Please try again.")  # Ask for a valid choice

# Entry point check — only run main if this script is executed directly
if __name__ == "__main__":
    main()
