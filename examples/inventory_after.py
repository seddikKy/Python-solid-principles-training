from abc import ABC, abstractmethod


class ProductInterface(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def calculate_total_price(self):
        pass

class Product(ProductInterface):
    def calculate_total_price(self):
        return self.price * self.quantity


class DiscountedProduct(ProductInterface):
    def __init__(self, name, price, quantity, discount_rate):
        super().__init__(name, price, quantity)
        self.discount_rate = discount_rate

    def calculate_total_price(self):
        discounted_price = self.price - (self.price * self.discount_rate)
        return discounted_price * self.quantity
    

class InventoryInterface(ABC):
    def __init__(self):
        self.products = []

    @abstractmethod
    def add(self, product):
        pass

    def remove(self, product):
        pass

    def display_inventory(self):
        return InventoryDisplay.display(self.products)
    
    def calculate_total(self):
        total_value = 0
        for product in self.products:
            total_value += product.calculate_total_price()
        return total_value



class Inventory(InventoryInterface):
    def add(self, product):
        self.products.append(product)
    
    def remove(self, product):
        self.products.remove(product)



class InventoryDisplay:
    @staticmethod
    def display(products):
        for product in products:
            print(f"{product.name}: {product.quantity} units, Total Price: {product.calculate_total_price()}")


class ReportGenerator:
    def generate_inventory_report(self, inventory):
        total_value = inventory.calculate_total()
        print(f"Total Inventory Value: {total_value}")


# Exemple d'utilisation
inventory = Inventory()

product1 = Product("Laptop", 1000, 5)
product2 = DiscountedProduct("Mouse", 20, 10, 0.1)

inventory.add(product1)
inventory.add(product2)

inventory.display_inventory()

report_generator = ReportGenerator()
report_generator.generate_inventory_report(inventory)
