class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.calculate_total_price()
        return total_value

    def display_inventory(self):
        for product in self.products:
            print(f"{product.name}: {product.quantity} units, Total Price: {product.calculate_total_price()}")


class DiscountedProduct(Product):
    def __init__(self, name, price, quantity, discount_rate):
        super().__init__(name, price, quantity)
        self.discount_rate = discount_rate

    def calculate_total_price(self):
        discounted_price = self.price - (self.price * self.discount_rate)
        return discounted_price * self.quantity


class ReportGenerator:
    def generate_inventory_report(self, inventory):
        total_value = inventory.calculate_total_inventory_value()
        print(f"Total Inventory Value: {total_value}")


# Exemple d'utilisation
inventory = Inventory()

product1 = Product("Laptop", 1000, 5)
product2 = DiscountedProduct("Mouse", 20, 10, 0.1)

inventory.add_product(product1)
inventory.add_product(product2)

inventory.display_inventory()

report_generator = ReportGenerator()
report_generator.generate_inventory_report(inventory)
