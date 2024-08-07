import json
from datetime import datetime
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self.expenses = defaultdict(list)
        self.filename = 'expenses.json'

    def add_expense(self, amount, category, description):
        try:
            expense = {
                'amount': float(amount),
                'category': category,
                'description': description,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self.expenses[category].append(expense)
            self.save_expenses()
            print("Expense added successfully.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file)

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            print("No previous expense records found. Starting fresh.")

    def show_expenses(self):
        for category, expenses in self.expenses.items():
            print(f"\nCategory: {category}")
            for expense in expenses:
                print(f"  Amount: {expense['amount']}, Description: {expense['description']}, Date: {expense['date']}")

    def category_summary(self):
        summary = defaultdict(float)
        for category, expenses in self.expenses.items():
            for expense in expenses:
                summary[category] += expense['amount']
        
        print("\nCategory-wise Summary:")
        for category, total in summary.items():
            print(f"  {category}: {total}")

    def monthly_summary(self):
        monthly_expenses = defaultdict(float)
        current_month = datetime.now().strftime('%Y-%m')

        for category, expenses in self.expenses.items():
            for expense in expenses:
                if expense['date'].startswith(current_month):
                    monthly_expenses[category] += expense['amount']
        
        print("\nMonthly Summary:")
        for category, total in monthly_expenses.items():
            print(f"  {category}: {total}")

def main():
    tracker = ExpenseTracker()
    tracker.load_expenses()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.show_expenses()
        elif choice == '3':
            tracker.category_summary()
        elif choice == '4':
            tracker.monthly_summary()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
