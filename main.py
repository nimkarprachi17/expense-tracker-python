def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully.")
#--------------------
def see_expense(expenses):
        if not expenses:
            print("No expenses recorded.")
            return

        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['category']} - ₹{expense['amount']}")
#---------------------
def total_expense(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print("Total spending: ₹", total)
#----------------------------
def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['amount']},{expense['category']}\n")
#--------------------
def load_expenses():
    expenses = []

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category = line.strip().split(",")
                expenses.append({
                    "amount": float(amount),
                    "category": category
                })
    except FileNotFoundError:
        pass

    return expenses            
#----------------------------
def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            see_expense(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break

        else:
            print("Invalid choice")

main()