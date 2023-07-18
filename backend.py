# Author: Bertan Berker
# Language: Python
# This is the backend for the online income statement maker

# These are for storing the necessary parts of the income statement
expenses = []
revenue = []
gains = []
losses = []
net_income = []


# This function adds the description and amount of money to revenue
def add_revenue(description, amount):
    rev = description + " - $" + amount
    net_income.append(amount)
    revenue.append(rev)

def get_revenue():
    return revenue


# This function adds the description and amount of money to expenses
def add_expense(description, amount):
    expense = description + " - $" + amount
    net_income.append("-" + amount)
    expenses.append(expense)

def get_expenses():
    return expenses


# This function adds the descrpt and amount of money to gains
def add_gains(description, amount):
    gain = description + " - $" + amount
    net_income.append(amount)
    gains.append(gain)

def get_gains():
    return gains


# This function adds the descript and amount of money to losses
def add_losses(description, amount):
    loss = description + " - $" + amount
    net_income.append("-" + amount)
    losses.append(loss)

def get_losses():
    return losses


# This function calculates the net income
# net income = (revenue + gains) - (expenses + losses)
def calculate_income():
    total = 0

    for val in net_income:
        
        if val[0] == '-':  # negative
            total -= int(val[1:])
        else:
            total += int(val)
        
    return total