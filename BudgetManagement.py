
from my_budgetcategory import BudgetCategory

def select_budget_category():
    while True:
        if not budget_categories:
            print("No budget categories available.")
            return None

        print("Available budget categories:")
        for index, category_name in enumerate(budget_categories.keys()):
            print(f"{index}: {category_name}")

        try:
            selected_index = int(input("Enter the index of the category: "))
            selected_category_name = list(budget_categories.keys())[selected_index]
            return selected_category_name
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")

def display_categories_by_type(budget_type):
    print(f"\nDisplaying {budget_type} budget categories:")
    for category in budget_categories.values():
        if category.get_budget_type() == budget_type:
            category.display_category_summary()

# Dictionary to store budget categories
budget_categories = {}

while True:
    print("\nBudget Management System")
    print("1. Add budget category")
    print("2. Set allocated budget")
    print("3. Add expenses")
    print("4. Display budget details")
    print("5. View remaining budget")
    print("6. View categories by budget type")
    print("7. Exit application")
    
    action = input("Enter your selection: ")
    
    if action == '7':
        print("Exiting application. Goodbye")
        break
    
    try:
        if action == '1':
            category_name = input("Enter the budget category name: ")
            budget_category = BudgetCategory(category_name)
            budget_categories[category_name] = budget_category
            print("Budget category added.")
        
        elif action == '2':
            selected_category_name = select_budget_category()
            if selected_category_name:
                selected_category = budget_categories[selected_category_name]
                selected_category.input_budget_type()
                while True:
                    try:
                        allocated_budget = float(input(f"Enter the allocated budget for {selected_category_name}: "))
                        selected_category.set_allocated_budget(allocated_budget)
                        print(f"Allocated budget for {selected_category_name} updated.")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the budget.")
        
        elif action == '3':
            selected_category_name = select_budget_category()
            if selected_category_name:
                selected_category = budget_categories[selected_category_name]
                while True:
                    try:
                        expense = float(input(f"Enter the expense amount for {selected_category_name}: "))
                        description = input("Enter a description for the expense: ")
                        selected_category.add_expense(expense, description)
                        print("Expense added.")
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the expense.")
        
        elif action == '4':
            for category in budget_categories.values():
                category.display_category_summary()
        
        elif action == '5':
            selected_category_name = select_budget_category()
            if selected_category_name:
                selected_category = budget_categories[selected_category_name]
                remaining_budget = selected_category.get_remaining_budget()
                print(f"Remaining budget for {selected_category_name}: ${remaining_budget}")
                
        elif action == '6':
            print("\nView categories by budget type")
            print("1. Weekly")
            print("2. Monthly")
            while True:
                budget_type_action = input("Enter your selection: ")
                if budget_type_action == '1':
                    display_categories_by_type('Weekly')
                    break
                elif budget_type_action == '2':
                    display_categories_by_type('Monthly')
                    break
                else:
                    print("Invalid selection. Please try again.")
        
        else:
            print("Invalid selection. Please try again.")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
