"""
Module: product_categories.py

This module defines classes representing different product categories.

Classes:
- Product (Parent Class): Represents a generic product with basic attributes and methods.
- Book (Sub-class): Represents a specific type of product - a book, inheriting from Product.
- Electronics (Sub-class): Represents another specific type of product - electronics, inheriting from Product.
- Clothing (Sub-class): Represents yet another specific type of product - clothing, inheriting from Product.

Usage:
Each class provides methods to interact with product attributes and display product information.

"""
class Product:
    def __init__(self, product_id, title, name, price, quantity):
        self.product_id = product_id
        self.title = title
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sold_quantity = 0  # Track quantity sold

    def display(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Title: {self.title}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Quantity Sold: {self.sold_quantity}")

    def get_product_id(self):
        return self.product_id
    
    def get_title(self):
        return self.title

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_sold_quantity(self):
        return self.sold_quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    def sell(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            self.sold_quantity += quantity
        else:
            raise ValueError("Insufficient quantity")


class Book(Product):
    def __init__(self, product_id, title, author, price, quantity):
        super().__init__(product_id, title, title, price, quantity)  # Use title as name for Book
        self.author = author

    def display(self):
        print(f"Product ID: {self.product_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Quantity Sold: {self.sold_quantity}")


class Electronics(Product):
    def __init__(self, product_id, name, specs, price, quantity):
        super().__init__(product_id, name, name, price, quantity)  # Use name as the name for Electronics
        self.specs = specs

    def display(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")  
        print(f"Specs: {self.specs}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Quantity Sold: {self.sold_quantity}")


class Clothing(Product):
    def __init__(self, product_id, name, size, price, quantity):
        super().__init__(product_id, name, name, price, quantity)  # Use name as the name for Clothing
        self.size = size

    def display(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")  
        print(f"Size: {self.size}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Quantity Sold: {self.sold_quantity}")
