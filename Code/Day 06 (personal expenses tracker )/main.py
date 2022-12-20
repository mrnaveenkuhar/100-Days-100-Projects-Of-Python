# ----------------------------| 100 Days of Code |----------------------------#


print("Welcome to the expense tracker! Please enter your expenses for the month.")
r = int(input("what is your rent?\n--> "))
u = int(input("what is your utilities? \n--> "))
g = int(input("what is your groceries? \n--> "))
e = int(input("what is your entertainment? \n--> "))


def calculate_expenses(expenses):
    total_expenses = 0

    # Calculate the total expenses by summing the values in the expenses dictionary

    for expense in expenses.values():
        total_expenses += expense

    return total_expenses


expenses = {"rent": r, "utilities": u, "groceries": g, "entertainment": e}
total_expenses = calculate_expenses(expenses)
print(f"Total expenses: {total_expenses}")
