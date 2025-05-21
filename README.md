
# 💰 Personal Expense Tracker (GUI App)

This is a GUI-based **Personal Expense Tracker** built using **Python** and **Tkinter**. It allows users to record daily expenses, view them, filter by month/year, get monthly summaries, and receive basic financial advice based on their spending patterns.

---

## 📌 Features

- 🧾 Add expense details (amount, category, date, description)
- 📄 View all stored expenses
- 🔍 Filter expenses by month and year
- 📊 Monthly expense summary
- 🧠 Automated financial advice based on spending
- 🖥️ User-friendly GUI using Tkinter

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** (GUI)
- **CSV** (for storing expense records)
- **Custom modules** for backend logic (e.g., `expense_manager.py`)

---

## 📁 Project Structure

```
personal-expense-tracker/
│
├── expense_tracker.py         # Main GUI application
├── expense_manager.py         # Backend logic (add, view, filter, summarize)
├── expenses.csv               # Stores all the expense records
└── README.md                  # Project documentation
```

---

## 🚀 How to Run the Project

1. **Clone this repository** or download the files.
2. Ensure Python is installed (preferably Python 3.10 or later).
3. Run the GUI app using the terminal or your IDE:

```bash
python expense_tracker.py
```

---

## 🧪 Example Use Case

### Add Expense
```
Amount: 500  
Category: Food  
Date: 2025-05-20  
Description: Grocery shopping
```

### Filter & Advice
- Filter by May 2025
- Get summary and advice like:
  - "You spent over ₹10,000 this month. Reduce discretionary spending."
  - "Your Food expense is over ₹3000. Consider home-cooked meals."

---

## ✅ To-Do / Future Scope

- Add support for **SQLite/MySQL** for persistent storage
- Add **Pie charts/graphs** using `matplotlib` or `Plotly`
- Create **export to Excel/PDF** feature
- Add **user login/authentication**
- Implement **dark mode** and enhanced UI

---

## 📷 Screenshots

*Add GUI screenshots here if needed.*

---

## 👨‍💻 Author

Made with ❤️ by **Dashmeet Singh**  
Feel free to connect and contribute!

---

## 📃 License

This project is open-source and free to use for learning purposes.
