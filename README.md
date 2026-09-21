# Student Expense Tracker

## Project Description

Student Expense Tracker is a beginner-level Python console application. It helps students record expenses, view saved expenses, calculate total spending, and search expenses by category.

The project uses a simple Python list of dictionaries to store expense details while the program is running.

## Features

- Add a new expense
- View all expenses
- Calculate total expenses
- Search expenses by category
- Validate amount, category, and description
- Simple menu-based console interface

## Technologies Used

- Python
- Console input and output
- No external libraries

## How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal or command prompt in this project folder.
3. Run the program:

```bash
python student_expense_tracker.py
```

If your system uses `python3`, run:

```bash
python3 student_expense_tracker.py
```

## Example Output

```text
Student Expense Tracker
1. Add Expense
2. View All Expenses
3. Calculate Total Expenses
4. Search Expense by Category
5. Exit
Enter your choice: 1
Enter amount: 120
Enter category: Food
Enter description: Lunch
Enter date (DD-MM-YYYY): 21-09-2026
Expense added successfully!

Student Expense Tracker
1. Add Expense
2. View All Expenses
3. Calculate Total Expenses
4. Search Expense by Category
5. Exit
Enter your choice: 2
---------------------------------------------
No.   Amount   Category   Description   Date
---------------------------------------------
1     ₹120     Food       Lunch         21-09-2026
---------------------------------------------
```

## Python Concepts Learned

- Variables
- Strings
- Integers and floats
- Lists
- Dictionaries
- Functions
- `if`, `elif`, and `else`
- `while` loops
- `for` loops
- `try` and `except`
- User input

## Future Improvements

- Save expenses to a file
- Add date validation
- Edit or delete expenses
- Show category-wise totals
- Add monthly expense reports
