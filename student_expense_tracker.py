import sys


try:
    sys.stdout.reconfigure(encoding="utf-8")
except AttributeError:
    pass


expenses = []


def add_expense():
    """Ask the user for expense details and save the expense."""
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    category = input("Enter category: ").strip()
    while category == "":
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    description = input("Enter description: ").strip()
    while description == "":
        print("Description cannot be empty.")
        description = input("Enter description: ").strip()

    date = input("Enter date (DD-MM-YYYY): ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    """Display all saved expenses."""
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("---------------------------------------------")
    print("No.   Amount   Category   Description   Date")
    print("---------------------------------------------")

    for index, expense in enumerate(expenses, start=1):
        amount = format_amount(expense["amount"])
        print(f"{index:<5} ₹{amount:<7} {expense['category']:<10} {expense['description']:<13} {expense['date']}")

    print("---------------------------------------------")


def calculate_total():
    """Calculate and display total expenses."""
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expenses: ₹{format_amount(total)}")


def search_by_category():
    """Search and display expenses for a category."""
    search_category = input("Enter category: ").strip().lower()
    matching_expenses = []

    for expense in expenses:
        if expense["category"].lower() == search_category:
            matching_expenses.append(expense)

    if len(matching_expenses) == 0:
        print("No expenses found in this category.")
        return

    print("---------------------------------------------")
    print("No.   Amount   Category   Description   Date")
    print("---------------------------------------------")

    for index, expense in enumerate(matching_expenses, start=1):
        amount = format_amount(expense["amount"])
        print(f"{index:<5} ₹{amount:<7} {expense['category']:<10} {expense['description']:<13} {expense['date']}")

    print("---------------------------------------------")


def format_amount(amount):
    """Show whole numbers without decimal places."""
    if amount == int(amount):
        return int(amount)

    return amount


def main():
    """Run the Student Expense Tracker menu."""
    while True:
        print("\nStudent Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Search Expense by Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            search_by_category()
        elif choice == "5":
            print("Thank you for using Student Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
