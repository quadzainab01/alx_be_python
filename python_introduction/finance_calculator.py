# finance_calculator.py

# Prompt user for financial details
monthly_income = float(input("Enter your monthly income: "))

monthly_expenses = float(input("Enter your total monthly expenses: "))


# Calculate monthly savings by subtracting monthly_expenses from monthly_income
monthly_savings = monthly_income - monthly_expenses


# Project annual savings with 5% annual simple interest rate for 1 year (12 months)
annual_savings = monthly_savings * 12

annual_interest = annual_savings * 0.05

projected_savings = annual_savings + annual_interest


# Output results
print(f"Your monthly savings are ${monthly_savings}.")

print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
