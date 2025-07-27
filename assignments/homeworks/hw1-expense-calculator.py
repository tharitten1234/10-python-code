"""
Personal Finance Calculator
Student: [Your Name]
Date: [Today's Date]
Purpose: Calculate monthly budget and savings
"""

# รับข้อมูลจากผู้ใช้
monthly_income = float(input("Enter your monthly income (THB): "))
rent_cost = float(input("Enter your rent cost (THB): "))
food_budget = int(input("Enter your food budget (THB): "))
transportation_cost = float(input("Enter your transportation cost (THB): "))
entertainment_budget = int(input("Enter your entertainment budget (THB): "))
emergency_percent = float(input("Enter emergency fund percent (e.g. 10.0): "))
investment_percent = float(input("Enter investment percent (e.g. 15.0): "))

# คำนวณค่าใช้จ่าย
fixed_expenses = rent_cost + transportation_cost
variable_expenses = food_budget + entertainment_budget
total_expenses = fixed_expenses + variable_expenses
remaining_income = monthly_income - total_expenses

# คำนวณเงินออม
emergency_fund = monthly_income * (emergency_percent / 100)
investment = monthly_income * (investment_percent / 100)
available_savings = remaining_income - emergency_fund - investment

# คำนวณ Expense Ratio
expense_ratio = (total_expenses / monthly_income) * 100

# แสดงผล
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {fixed_expenses:.2f} THB")
print(f"Variable Expenses: {variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_percent}%): {emergency_fund:.2f} THB")
print(f"Investment ({investment_percent}%): {investment:.2f} THB")
print(f"Available for Savings: {available_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")
