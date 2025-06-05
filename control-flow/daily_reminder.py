task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

print("Reminder:")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Try to handle it as soon as possible.")
    case "medium":
        if time_bound.strip == "yes":
            print(f"'{task}' is a medium priority task that should be completed today.")
        else:
            print(f"'{task}' is a medium priority task. Plan to do it this week.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task, but it still requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered.")

