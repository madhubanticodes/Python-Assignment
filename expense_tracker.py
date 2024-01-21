import json
from datetime import datetime

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = {"categories": [], "transactions": []}
    return expenses

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)

def show_categories(expenses):
    print("Expense Categories:")
    for category in expenses["categories"]:
        print(f"- {category}")

def add_expense(expenses, category, amount, description):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = {"timestamp": timestamp, "category": category, "amount": amount, "description": description}
    expenses["transactions"].append(transaction)

    if category not in expenses["categories"]:
        expenses["categories"].append(category)

    print("Expense added successfully.")
    save_expenses(expenses)

def show_transactions(expenses):
    if not expenses["transactions"]:
        print("No transactions found.")
    else:
        print("Expense Transactions:")
        for transaction in expenses["transactions"]:
            print(f"{transaction['timestamp']} - {transaction['category']} - ${transaction['amount']} - {transaction['description']}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Show Expense Categories")
        print("2. Add Expense")
        print("3. Show Expense Transactions")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_categories(expenses)
        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: $"))
            description = input("Enter expense description: ")
            add_expense(expenses, category, amount, description)
        elif choice == "3":
            show_transactions(expenses)
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
