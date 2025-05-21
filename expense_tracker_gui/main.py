import tkinter as tk
from tkinter import messagebox
from expense_manager import add_expense, view_expenses, filter_by_month, get_summary, get_local_advice

# Create the main window
root = tk.Tk()
root.title("Personal Expense Tracker")

# Set window size
root.geometry("600x500")

# Add Expense Function
def add_expense_gui():
    try:
        amount = float(entry_amount.get())
        category = entry_category.get()
        date = entry_date.get()
        description = entry_description.get()
        add_expense('expenses.csv', amount, category, date, description)
        messagebox.showinfo("Success", "Expense added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please check your entries.")

# View Expenses Function
def view_expenses_gui():
    expenses_window = tk.Toplevel(root)
    expenses_window.title("View Expenses")

    expenses_list = view_expenses('expenses.csv')

    listbox = tk.Listbox(expenses_window, width=80, height=20)
    listbox.pack()

    for expense in expenses_list:
        listbox.insert(tk.END, expense)

# Filter by Month/Year Function
def filter_by_month_gui():
    try:
        month = int(entry_month.get())
        year = int(entry_year.get())
        expenses = filter_by_month('expenses.csv', month, year)

        # Clear the listbox to show filtered data
        listbox.delete(0, tk.END)
        for expense in expenses:
            listbox.insert(tk.END, expense)
    except ValueError:
        messagebox.showerror("Error", "Invalid month/year input.")

# Summary Function
def summary_gui():
    try:
        month = int(entry_month.get())
        year = int(entry_year.get())
        total_spent = get_summary('expenses.csv', month, year)
        messagebox.showinfo("Monthly Summary", f"Total spent in {month}/{year}: ₹{total_spent}")
    except ValueError:
        messagebox.showerror("Error", "Invalid month/year input.")

# Advice Function
def advice_gui():
    try:
        month = int(entry_month.get())
        year = int(entry_year.get())
        advice = get_local_advice('expenses.csv', month, year)

        # Show advice in a new window
        advice_window = tk.Toplevel(root)
        advice_window.title("Financial Advice")

        listbox_advice = tk.Listbox(advice_window, width=80, height=20)
        listbox_advice.pack()

        for expense in advice['expenses']:
            listbox_advice.insert(tk.END, expense)

        listbox_advice.insert(tk.END, f"\nTotal spent: ₹{advice['total_spent']}")
        
        # Local Financial Advice
        if advice['total_spent'] > 10000:
            listbox_advice.insert(tk.END, "You have exceeded ₹10,000 this month. Consider reducing your discretionary spending.")
        if 'Food' in advice['categories'] and advice['categories']['Food'] > 3000:
            listbox_advice.insert(tk.END, "You are spending a lot on Food. Try to cook at home more to save.")
        if 'Entertainment' in advice['categories'] and advice['categories']['Entertainment'] > 2000:
            listbox_advice.insert(tk.END, "Your entertainment expenses are high. Consider reducing subscription services or dining out less.")
        if 'Transportation' in advice['categories'] and advice['categories']['Transportation'] > 2000:
            listbox_advice.insert(tk.END, "Your transportation expenses are high. Try using public transport or carpooling to save.")
        if advice['total_spent'] < 5000:
            listbox_advice.insert(tk.END, "Great job! You're keeping your spending low. Keep it up!")
    except ValueError:
        messagebox.showerror("Error", "Invalid month/year input.")

# GUI Widgets
label_amount = tk.Label(root, text="Amount: ")
label_amount.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

label_category = tk.Label(root, text="Category: ")
label_category.pack()

entry_category = tk.Entry(root)
entry_category.pack()

label_date = tk.Label(root, text="Date (YYYY-MM-DD): ")
label_date.pack()

entry_date = tk.Entry(root)
entry_date.pack()

label_description = tk.Label(root, text="Description: ")
label_description.pack()

entry_description = tk.Entry(root)
entry_description.pack()

button_add = tk.Button(root, text="Add Expense", command=add_expense_gui)
button_add.pack()

label_month = tk.Label(root, text="Month (1-12): ")
label_month.pack()

entry_month = tk.Entry(root)
entry_month.pack()

label_year = tk.Label(root, text="Year: ")
label_year.pack()

entry_year = tk.Entry(root)
entry_year.pack()

button_view = tk.Button(root, text="View Expenses", command=view_expenses_gui)
button_view.pack()

button_filter = tk.Button(root, text="Filter by Month/Year", command=filter_by_month_gui)
button_filter.pack()

button_summary = tk.Button(root, text="Monthly Summary", command=summary_gui)
button_summary.pack()

button_advice = tk.Button(root, text="Get Financial Advice", command=advice_gui)
button_advice.pack()

button_exit = tk.Button(root, text="Exit", command=root.quit)
button_exit.pack()

# Run the application
root.mainloop()
