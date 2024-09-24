import random  # Importing the random module to generate random product identifiers.

# Defining a base class called Product.
class Product():
    # Constructor method to initialize product attributes: name, price, weight, flammability, and a random identifier.
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        # Setting the product's name, price, weight, and flammability with default values.
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        # Generating a random identifier between 1,000,000 and 9,999,999 for each product.
        self.identifier = random.randint(1000000, 9999999)

    # Method to calculate and return the product's "stealability" based on the price/weight ratio.
    def stealability(self):
        # Calculating the ratio of price to weight.
        ratio = self.price / self.weight
        # Conditional logic to determine stealability based on the ratio.
        if ratio < 0.5:
            return "Not so stealable..."  # If ratio is less than 0.5, it's not very stealable.
        elif ratio < 1.0:
            return "Kinda stealable."  # If ratio is between 0.5 and 1.0, it's moderately stealable.
        else:
            return "Very stealable!"  # If ratio is 1.0 or higher, it's very stealable.

    # Method to calculate and return the product's explosiveness based on flammability and weight.
    def explode(self):
        # Calculating the product of flammability and weight to determine explosiveness.
        product = self.flammability * self.weight
        # Conditional logic to determine the explosiveness based on the calculated value.
        if product < 10:
            return "..fizzle."  # If the value is less than 10, it's a weak explosion.
        elif product < 50:
            return "..boom!"  # If the value is between 10 and 50, it's a moderate explosion.
        else:
            return "BABOOM!!"  # If the value is 50 or greater, it's a big explosion.

# Defining a subclass called BoxingGlove that inherits from the Product class.
class BoxingGlove(Product):
    # Constructor method that initializes BoxingGlove-specific attributes and calls the parent Product class constructor.
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        # Calling the parent class's constructor with boxing glove-specific default values.
        super().__init__(name, price, weight, flammability)

    # Overriding the explode method specifically for boxing gloves.
    def explode(self):
        # Boxing gloves don't explode, so the method always returns this message.
        return "...it's a glove."

    # Method to simulate a punch, returning a response based on the weight of the glove.
    def punch(self):
        # Conditional logic to determine the punch effect based on the glove's weight.
        if self.weight < 5:
            return "That tickles."  # If the glove's weight is less than 5, the punch is weak.
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"  # If the weight is between 5 and 15, the punch is moderate.
        else:
            return "OUCH!"  # If the weight is 15 or more, the punch is strong.

class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
