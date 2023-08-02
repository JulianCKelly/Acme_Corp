import random
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Bed']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        product = Product(name, price=price, weight=weight,
                          flammability=flammability)
        products.append(product)
    return products


def inventory_report(products):
    names = set()
    total_price = 0
    total_weight = 0
    total_flammability = 0
    for product in products:
        names.add(product.name)
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability
    num_unique_names = len(names)
    avg_price = total_price / len(products)
    avg_weight = total_weight / len(products)
    avg_flammability = total_flammability / len(products)

    return (num_unique_names, avg_price, avg_weight, avg_flammability)


if __name__ == '__main__':
    print(inventory_report(generate_products()))
