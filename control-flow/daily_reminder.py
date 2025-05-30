# Prompt for user inputs
task = input("Enter your task: ").strip()
priority = get_input("Priority (high/medium/low): ", ["high", "medium", "low"])
time_bound = get_input("Is it time-bound? (yes/no): ", ["yes", "no"])

# Generate customized reminder
print("\nReminder:")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Try to handle it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task that should be completed today.")
        else:
            print(f"'{task}' is a medium priority task. Plan to do it this week.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task, but it still requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
