def add_new_expense(expense_list):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully.")
#--------------------
def show_expense(expenses):
        if not expenses:
            print("No expenses recorded.")
            return

        for index, item in enumerate(expense_list, start=1):
            print(f"{index}. {expense['category']} - ₹{expense['amount']}")
        print("Total number of expenses:", len(expense_list))
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
        print("\n------ Personal Expense Tracker ------")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Total")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_new_expense(expenses)

        elif choice == "2":
            show_expense(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break

        else:
            print("Invalid choice")

main()
