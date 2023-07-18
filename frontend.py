# Author: Bertan Berker
# Language: Python
# This is the frontend for the income statement template that I create with tkinter

import tkinter as tk
from backend import add_expense, get_expenses, add_revenue, get_revenue, get_gains, get_losses, add_gains, add_losses,calculate_income


# This function completes the necessary error check when user submits a value
def error_check():
    if description_entry.get() == "":
        message_var.set("Empty Description! Please fill out this section...")
        return False
    
    elif amount_entry.get() == "":
        message_var.set("No Amount Specified! Please fill out this section...")
        return False
    
    for val in amount_entry.get():
        if not val.isdigit():
            message_var.set("Invalid Amount! Amount has to be a valid number...")
            return False
        
    message_var.set("Addition to the system is complete...")
    return True


def add_revenue_click():
    if error_check():
        description = description_entry.get()
        amount = amount_entry.get()
        add_revenue(description, amount)
        update_net_income()
        update_revenue_list()


def update_revenue_list():
    revenue_list.delete(0, tk.END)
    revenue = get_revenue()
    for rev in revenue:
        revenue_list.insert(tk.END, rev)


def add_expense_click():
    if error_check():
        description = description_entry.get()
        amount = amount_entry.get()
        add_expense(description, amount)
        update_net_income()
        update_expense_list()


def update_expense_list():
    expense_list.delete(0, tk.END)
    expenses = get_expenses()
    for expense in expenses:
        expense_list.insert(tk.END, expense)


def add_gains_click():
    if error_check():
        description = description_entry.get()
        amount = amount_entry.get()
        add_gains(description, amount)
        update_net_income()
        update_gains_list()


def update_gains_list():
    gains_list.delete(0, tk.END)
    gains = get_gains()
    for gain in gains:
        gains_list.insert(tk.END, gain)
        
       
def add_losses_click():
    if error_check():
        description = description_entry.get()
        amount = amount_entry.get()
        add_losses(description, amount)
        update_net_income()
        update_losses_list()

def update_losses_list():
    losses_list.delete(0, tk.END)
    losses = get_losses()
    for loss in losses:
        losses_list.insert(tk.END, loss)

def update_net_income():
    net_income = calculate_income()
    net_income_var.set('$' + str(net_income))


def on_closing():
    root.destroy()

root = tk.Tk()
root.title("Expense Tracker")
root.attributes("-fullscreen", True)  # Make the window fullscreen

quit_button = tk.Button(root, text="X", background = "red", fg="white", font= 22, command=on_closing)
quit_button.place(x=root.winfo_screenwidth() - 40, y=0, width=40, height=40)
root.protocol("WM_DELETE_WINDOW", on_closing)


description_label = tk.Label(root, text="Description:", font=("Arial", 16))
description_label.grid(row=18, column=0, sticky="w")

description_entry = tk.Entry(root, font=("Arial", 16))
description_entry.grid(row=19, column=0, sticky="w")

amount_label = tk.Label(root, text="Amount:", font=("Arial", 16))
amount_label.grid(row=20, column=0, sticky="w")

amount_entry = tk.Entry(root, font=("Arial", 16))
amount_entry.grid(row=21, column=0, sticky="w")

rev_button = tk.Button(root, text="Add Revenue", command=add_revenue_click)
rev_button.grid(row=25, column=0, sticky="w", padx=10)

ex_button = tk.Button(root, text="Add Expense", command=add_expense_click)
ex_button.grid(row=25, column=0, sticky="w", padx=100)

gains_button = tk.Button(root, text="Add Gains", command=add_gains_click)
gains_button.grid(row=26, column=0, sticky="w", padx=10)

losses_button = tk.Button(root, text="Add Losses", command=add_losses_click)
losses_button.grid(row=26, column=0, sticky="w", padx=100)

revenue_list_label = tk.Label(root, text="Revenue:")
revenue_list_label.grid(row=7, column=30)

revenue_list = tk.Listbox(root, width=50, height=10)
revenue_list.grid(row=8, column=30, rowspan=4, padx=10)

expense_list_label = tk.Label(root, text="Expenses:")
expense_list_label.grid(row=15, column=30)

expense_list = tk.Listbox(root, width=50, height=10)
expense_list.grid(row=16, column=30, rowspan=4, padx=10)

gains_list_label = tk.Label(root, text="Gains:")
gains_list_label.grid(row=23, column=30)

gains_list = tk.Listbox(root, width=50, height=10)
gains_list.grid(row=24, column=30, rowspan=4, padx=10)

losses_list_label = tk.Label(root, text="Losses:")
losses_list_label.grid(row=31, column=30)

losses_list = tk.Listbox(root, width=50, height=10)
losses_list.grid(row=32, column=30, rowspan=4, padx=10)

# Create a StringVar to hold the net income value
net_income_var = tk.StringVar()
net_income_var.set("$0")  # Initialize the net income to 0

# Create the net income label
net_income_label = tk.Label(root, text="Net Income:", font=("Arial", 16))
net_income_label.grid(row=50, column=30)

# Create the net income value label using the StringVar
net_income_value_label = tk.Label(root, textvariable=net_income_var, font=("Arial", 16))
net_income_value_label.grid(row=51, column=30)


# Create a StringVar to hold the message
message_var = tk.StringVar()
message_var.set("Hello, please use our program to calculate your net income")  # Initialize the net income to Intro

# Create the message label
message_label = tk.Label(root, text="Message:", font=("Arial", 16))
message_label.grid(row=20, column=1, sticky="e")

# Create the message value label using the StringVar
message_value_label = tk.Label(root, textvariable=message_var,font=("Arial", 16))
message_value_label.grid(row=20, column=2)


root.mainloop()
