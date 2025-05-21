import csv
from datetime import datetime

def add_expense(file_path, amount, category, date, description):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

def view_expenses(file_path):
    expenses = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append(row)
    return expenses

def filter_by_month(file_path, month, year):
    expenses = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
                if date.month == month and date.year == year:
                    expenses.append(row)
            except ValueError:
                pass  # Ignore rows with invalid date format
    return expenses

def get_summary(file_path, month, year):
    total = 0
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
                if date.month == month and date.year == year:
                    total += float(row[2])
            except ValueError:
                pass  # Ignore rows with invalid date format
    return total

def get_local_advice(file_path, month, year):
    expenses = []
    total_spent = 0
    categories = {}

    # Read expenses and collect data
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
                if date.month == month and date.year == year:
                    amount = float(row[2])
                    category = row[1]
                    expenses.append(f"- {row[0]}, {row[1]}, ₹{amount}")
                    total_spent += amount
                    
                    if category in categories:
                        categories[category] += amount
                    else:
                        categories[category] = amount
            except ValueError:
                pass  # Ignore rows with invalid date format

    advice = {
        "expenses": expenses,
        "total_spent": total_spent,
        "categories": categories
    }
    return advice
