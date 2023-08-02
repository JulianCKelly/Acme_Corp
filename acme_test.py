from acme import Product
from acme_report import generate_products


def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_attributes():
    '''Test default product attributes.'''
    prod = Product('Test Product')
    assert prod.weight == 20
    assert prod.flammability == 0.5
    assert isinstance(prod.name, str)


def test_product_stealability():
    '''Test stealability method.'''
    prod = Product('Test Product', price=20, weight=10)
    assert prod.stealability() == 'Very stealable!'

    if prod.stealability() == 'Very stealable!':
        return 'TRUE'
    else:
        return 'FALSE'


def test_product_explode():
    '''Test explode method.'''
    prod = Product('Test Product', flammability=2.5, weight=10)
    assert prod.explode() == '...BABOOM!!'

    if prod.explode() == '...BABOOM!!':
        return 'TRUE'
    else:
        return 'FALSE'


def test_generate_products():
    '''Test generate_products function.'''
    products = generate_products()
    for product in products:
        assert isinstance(product, Product)
