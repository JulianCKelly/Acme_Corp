# Importing the Product class and generate_products function from their respective modules.
from acme import Product
from acme_report import generate_products


# Test case to check if the default price of a Product is 10.
def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')  # Create a product with default attributes
    assert prod.price == 10  # Assert that the default price is 10


# Test case to check if the default attributes of a Product are correctly set.
def test_default_product_attributes():
    '''Test default product attributes.'''
    prod = Product('Test Product')  # Create a product with default attributes
    assert prod.weight == 20  # Assert that the default weight is 20
    assert prod.flammability == 0.5  # Assert that the default flammability is 0.5
    assert isinstance(prod.name, str)  # Assert that the product's name is a string


# Test case to check the behavior of the stealability method in Product class.
def test_product_stealability():
    '''Test stealability method.'''
    prod = Product('Test Product', price=20, weight=10)  # Create a product with specific price and weight
    assert prod.stealability() == 'Very stealable!'  # Assert that the stealability method works as expected

    # Conditional block to return 'TRUE' or 'FALSE' based on stealability method's result.
    if prod.stealability() == 'Very stealable!':
        return 'TRUE'
    else:
        return 'FALSE'


# Test case to check the behavior of the explode method in Product class.
def test_product_explode():
    '''Test explode method.'''
    prod = Product('Test Product', flammability=2.5, weight=10)  # Create a product with specific flammability and weight
    assert prod.explode() == 'BABOOM!!'  # Assert that the explode method works as expected

    # Conditional block to return 'TRUE' or 'FALSE' based on explode method's result.
    if prod.explode() == 'BABOOM!!':
        return 'TRUE'
    else:
        return 'FALSE'


# Test case to check if generate_products creates a list of valid Product objects.
def test_generate_products():
    '''Test generate_products function.'''
    products = generate_products()  # Call the function to generate a list of products
    for product in products:
        assert isinstance(product, Product)  # Assert that each item in the list is a Product object
