#Expense Manager Console Application
##Overview
The Expense Manager is a Python-based console application designed to help users track their expenses efficiently. It provides a simple, text-based interface to add, view expenses and check monthly budget, with data persistence using a csv file. The application is ideal for users who prefer a lightweight, command-line tool for personal finance management.

##Features

Add Expense: Record a new expense with date, amount, category, and description.
View Expenses: List all recorded expenses with details.
Track Budget: Set monthly budget and verify if current month expences are over or under budget.
Save Expence: Save latest added expences to CSV file.
Data Persistence: Store expenses in a csv file for persistence between sessions.
User-Friendly Interface: Simple menu-driven navigation with input validation.

Implementation Details
The application is implemented in Python 3, utilizing standard libraries for file handling and data management. Below are the key components:
1. Data Storage

File Format: Expenses are stored in a csv file (expense.csv).
Structure: Each expense is a dictionary with fields: date, amount, category, and description.
Persistence: In filemanager.py get_data() and write_data() functions handle reading from and writing to the csv file.

2. Core Functions

Expence().add(): Prompts the user for expense details, validates inputs, and appends the expense to the list.
Expence.list(): Displays all expenses in a formatted table.
Expence.get_monthly_total(): Groups expenses by given month and year, calculating totals.
set_monthly_budget: Save limit of monthly budget.

3. User Interface

Menu: A loop displays a menu with options (1: Add Expense, 2: View Expenses, 3: Track budget, 4: Save Expense, 5: Exit).
Input Validation: Ensures valid numeric inputs for amounts and menu choices, and non-empty strings for categories and descriptions.
Error Handling: Gracefully handles file I/O errors and invalid inputs.

4. Dependencies

Standard Libraries:
csv: For reading/writing expenses to a file.
json: For reading/writing monthly budget to a file.
datetime: For handling dates.
io: For checking file existence.



5. Code Structure

Main Loop: The main() function runs the application, displaying the menu and calling appropriate functions based on user input.
Modularity: Functions are organized for specific tasks (e.g., add(), list()), ensuring maintainability.
Data Management: A list of expense dictionaries is maintained in memory, synced with the csv file.

Usage Instructions

Run the Python script (main.py).
Choose an option from the menu (1–5).
Follow prompts to add or view expenses, or set monthly budget.
Select option 5 to exit, automatically saving expenses to expenses.csv.

Example Interaction
Select an option:
	1:- Add Expense
	2:- View Expense
	3:- Track budget
	4:- Save Expense
	5:- Exit

: 1
Enter date (YYYY-MM-DD): 2025-05-11
Enter Category e.g. travel, food, other: travel
Enter amount e.g. 100.00: 50.00
Enter Description: meal
Expense added successfully.


Future Enhancements

Delete Expense: Add functionality to remove expenses by ID.
Edit Expense: Allow updating existing expense details.
Graphical Interface: Extend to a GUI using Tkinter or PyQt.
Budget Tracking: Implement budget limits and alerts.
Export Options: Support exporting summaries to CSV or PDF.

Conclusion
The Expense Manager console application provides a straightforward solution for tracking personal expenses. Its simplicity, combined with data persistence and summary features, makes it a practical tool for users seeking a minimalistic approach to expense management. The modular design allows for easy extension, catering to future enhancements as needed.
