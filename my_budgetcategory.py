"""
Module: my_budgetcategory.py

Purpose:
This module defines a `BudgetCategory` class for managing budget categories. 
It includes functionality for setting and getting budget details, adding expenses, 
and displaying budget summaries. The class is designed to help users track and manage 
their budget allocations effectively.

Classes:
- BudgetCategory: Represents a budget category with methods to manage and track the budget.
"""

# Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, name, budget=0, budget_type=None):
        self.__category_name = name
        self.__allocated_budget = budget
        self.__remaining_budget = budget
        self.__budget_type = budget_type
        self.__budget_types = ['Weekly', 'Monthly']
        self.__expenses = []  # List to store expenses

# Task 2: Setters and Getters Implementation
    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, name):
        self.__category_name = name

    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, budget):
        if budget > 0:
            self.__allocated_budget = budget
            self.__remaining_budget = budget
        else:
            raise ValueError("Budget must be a positive number")

    def get_remaining_budget(self):
        return self.__remaining_budget

    def get_budget_type(self):
        return self.__budget_type

    def set_budget_type(self, budget_type):
        if budget_type in self.__budget_types:
            self.__budget_type = budget_type
        else:
            raise ValueError("Invalid budget type")

# Task 3: Add expenses/budget functionality
    def add_expense(self, amount, description=""):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                self.__expenses.append((amount, description))  # Store expense with description
            else:
                raise ValueError("Expense exceeds remaining budget")
        else:
            raise ValueError("Expense amount must be a positive number")

    def get_total_expenses(self):
        return sum(amount for amount, description in self.__expenses)

# Task 4: Display budget details
    def display_category_summary(self):
        print(f"Category: {self.get_category_name()}")
        print(f"Budget Type: {self.get_budget_type()}")
        print(f"Allocated Budget: ${self.get_allocated_budget()}")
        total_expenses = self.get_total_expenses()
        print(f"Total Expenses: ${total_expenses}")
        if not self.__expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for amount, description in self.__expenses:
                print(f"  - Amount: ${amount}, Description: {description}")
        print(f"Remaining Budget: ${self.get_remaining_budget()}")

    def input_budget_type(self):
        while True:
            print("Select budget type from the list:")
            for index, budget in enumerate(self.__budget_types):
                print(f"{index}: {budget}")

            try:
                budget_type_index = int(input("Enter the index of the budget type: "))
                selected_budget_type = self.__budget_types[budget_type_index]
                self.set_budget_type(selected_budget_type)
                print(f"Selected budget type: {selected_budget_type}")
                return selected_budget_type
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")
