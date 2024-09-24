import random  # Importing the random module to generate random values for product attributes
from acme import Product  # Importing the Product class from the acme module


# List of adjectives and nouns to create random product names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Bed']


# Function to generate a list of random products
def generate_products(num_products=30):
    """
    Generates a list of random Product instances.

    Parameters:
    num_products (int): The number of products to generate (default is 30).

    Returns:
    list: A list of randomly generated Product instances.
    """
    products = []
    # Loop to generate the specified number of products
    for _ in range(num_products):
        # Generate a random product name by combining an adjective and a noun
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        # Generate random values for price, weight, and flammability
        price = random.randint(5, 100)  # Price between 5 and 100
        weight = random.randint(5, 100)  # Weight between 5 and 100
        flammability = random.uniform(0.0, 2.5)  # Flammability between 0.0 and 2.5
        # Create a new Product instance with the random values
        product = Product(name, price=price, weight=weight, flammability=flammability)
        # Append the product to the list
        products.append(product)
    # Return the list of generated products
    return products


# Function to generate an inventory report
def inventory_report(products):
    """
    Generates a report on a list of products, calculating the number of unique product names,
    and the average price, weight, and flammability.

    Parameters:
    products (list): A list of Product instances.

    Returns:
    tuple: A tuple containing the number of unique product names, and the average price, weight, and flammability.
    """
    names = set()  # A set to store unique product names
    total_price = 0  # Variable to sum up all product prices
    total_weight = 0  # Variable to sum up all product weights
    total_flammability = 0  # Variable to sum up all product flammabilities

    # Loop through each product in the list
    for product in products:
        # Add the product's name to the set (ensures uniqueness)
        names.add(product.name)
        # Add the product's price, weight, and flammability to the total sums
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    # Calculate the number of unique product names
    num_unique_names = len(names)
    # Calculate the average price, weight, and flammability
    avg_price = total_price / len(products)
    avg_weight = total_weight / len(products)
    avg_flammability = total_flammability / len(products)

    # Return the report as a tuple
    return (num_unique_names, avg_price, avg_weight, avg_flammability)


# Main function to generate and print the inventory report
if __name__ == '__main__':
    # Generate a list of random products and print the inventory report
    print
