from datetime import datetime, date

def welcome_message():
    print("Welcome to the Expense Tracker!")

def enter_expense():
    expense = {}
    while True:
        try:
            amount = float(input("Please enter the amount of the expense: ")) 
            if amount <= 0:
                raise ValueError("Amount must be a positive number.")
            break
        except ValueError as e:
            print(e)
        
    category = input("Enter the expense category (Food, Transport, Entertainment, Home, Other): ")
   
    while True:
        date_str = input("Enter the date of expense (DD/MM/YYYY): ")
        try:
            expense_date = datetime.strptime(date_str, "%d/%m/%Y").date()

            if expense_date > date.today():
                raise ValueError("The date cannot be in the future.")
            break
        except ValueError as e:
            print(e)


    expense['amount'] = amount
    expense['category'] = category
    expense['date'] = expense_date
    return expense

def store_data(expense, expenses):
    expenses.append(expense)

def display_summary(expenses):
    total_spent = sum(exp['amount'] for exp in expenses)
    print(f"Total amount spent: £{total_spent:.2f}")

    category_summary = {}
    for exp in expenses:
        category = exp['category']
        category_summary[category] = category_summary.get(category, 0) + exp['amount']

    for category, total in category_summary.items():
        print(f"Total spent on {category}: £{total:.2f}")

    print("\nDetailed Expenses:")
    for exp in expenses:
        print(f"{exp['date'].strftime('%d/%m/%Y')}: £{exp['amount']} in {exp['category']}")

def validate_input():
    pass

def thanks_message():
    print("Thank you for using Expense Tracker!")

def main():
    welcome_message()
    expenses = []
    while True:
        expense = enter_expense()
        store_data(expense, expenses)
        another = input("Would you like to enter another expense? (yes/no): ")
        if another.lower() != 'yes':
            break

    display_summary(expenses)
    thanks_message()

if __name__ == "__main__":
    main()







            






