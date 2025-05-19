# Personal Finance Calculator

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${monthly_savings}")


# Simple Interest Calculator

rate = 0.05
years = 1

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * rate) ** years

print(f"Projected savings after one year, with interest, is: ${projected_savings}")