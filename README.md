## Software Engineering - My Acme Project
Welcome to my Acme Project! This repository contains code for organizing and managing products at Acme Corporation. In this project, I have written Python modules to handle products, generate reports, and perform tests.

# Part 1 - Keeping it Classy
I have created the acme.py module, which defines a class Product to model the products sold by Acme Corporation. Each product has the following attributes:

name (string with no default)
price (integer with default value 10)
weight (integer with default value 20)
flammability (float with default value 0.5)
identifier (integer - a randomly generated number from 1000000 to 9999999)

# Usage
To use the Product class, you can follow these steps:

Save the acme.py module.
In your Python REPL or script, import the Product class.
Create an instance of Product by providing a product name. Other attributes have default values but can be overridden if needed.
Example:


from acme import Product

prod = Product('A Cool Toy')
print(prod.name)        # Output: 'A Cool Toy'
print(prod.price)       # Output: 10
print(prod.weight)      # Output: 20
print(prod.flammability) # Output: 0.5
print(prod.identifier)   # Output: (random value between 1000000 and 9999999)

# Part 2 - Objects that Go!
The Product class is now enhanced with two methods:

stealability(self): I have implemented this method to calculate the price divided by the weight and return a corresponding message.
explode(self): I have implemented this method to calculate the flammability times the weight and return a corresponding message.

Usage
Once you have the Product class instance, you can use the new methods like this:

from acme import Product

prod = Product('A Cool Toy')
print(prod.stealability()) # Output: 'Kinda stealable.'
print(prod.explode())      # Output: '...boom!'

# Part 3 - A Proper Inheritance
I have created the BoxingGlove class as a child class of the Product class, specially designed for Acme's boxing gloves. It inherits some attributes from the Product class but overrides the default weight and explode() method. It also adds a new method, punch().

Usage
You can use the BoxingGlove class just like the Product class:

from acme import BoxingGlove

glove = BoxingGlove('Punchy the Third')
print(glove.price)     # Output: 10
print(glove.weight)    # Output: 10
print(glove.punch())   # Output: 'Hey that hurt!'
print(glove.explode()) # Output: "...it's a glove."

# Part 4 - Class Report
I have created the acme_report.py module, which contains functions to generate random products and print a summary of their statistics.

generate_products(num_products=30): This function generates a given number of products (default 30) and returns them as a list.
inventory_report(product_list): This function takes a list of products and returns a tuple holding some basic statistics about the list of products.

Usage
You can use the provided functions as follows:

from acme_report import generate_products, inventory_report

products = generate_products() # Generate 30 random products
report = inventory_report(products)

print("Number of unique product names:", report[0])
print("Average (mean) price:", report[1])
print("Average (mean) weight:", report[2])
print("Average (mean) flammability:", report[3])
# Part 5 - Measure twice, Test once
The acme_test.py module contains test functions for the Product class.

test_default_product_price(): This test function tests the default product price being 10.
I have added at least three more test functions to acme_test.py to test the Product class:
Test the product's default attributes.
Test the stealability() and explode() methods.
Test the default generate_products() function to ensure it returns a list with 30 items in it.

# Part 6 - Style it Up
I have made sure that my code follows the PEP8 style guidelines. I used a Python linter in my text editor to ensure that my code is properly formatted.

