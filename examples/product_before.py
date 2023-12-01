from enum import Enum


class ProductType(Enum):
    Digital = 1
    Package = 2
    Promotional = 3


class Product:

    def __init__(self, type_of_product, name, number_of_assets, discount, free):
        self._name = name
        self._type = type_of_product
        self._number_of_assets = number_of_assets
        self._discount = discount
        self._free = free

    def price(self):
        if self._type == ProductType.Digital:
            return self._base_price()
        if self._type == ProductType.Package:
            if self._number_of_assets > 2:
                return self._base_price() * self._number_of_assets * self._discount_factor()
            else:
                return max([100, self._base_price() * self._number_of_assets])
        if self._type == ProductType.Promotional:
            if self._free:
                return 0
            else:
                return self._calculate_base_price_with_discount(self._discount)

        raise ValueError("should be unreachable")

    def _calculate_base_price_with_discount(self, discount):
        return max([500, self._base_price() - self._base_price() * discount/100.0])

    def _discount_factor(self):
        return 0.9

    def _base_price(self):
        return 1000

    def to_json(self):
        return {
            'name': self._name,
            'type': self._type.value,
            'price': self.price(),
            'discount': self._discount,
            'free': self._free,
            'assets': self._number_of_assets
        }

  
    
# Exemple d'utilisation
products =  [
                Product(ProductType.Digital, "Digital 1", 0, 0, False).to_json(),
                Product(ProductType.Digital, "Digital 2", 0, 0, True).to_json(),
                Product(ProductType.Package, "Package 1", 5, 0, False).to_json(),
                Product(ProductType.Package, "Package 2", 10, 0, True).to_json(),
                Product(ProductType.Promotional, "Promo - Discounted Product", 0, 50, False).to_json(),
                Product(ProductType.Promotional, "Promo - Free product", 0, 0, True).to_json(),
            ]

for product in products:
    print(product)