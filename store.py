from products import Product
from typing import List, Tuple

class Store:
    """
    Represents a store that holds a list of products.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes the store with a list of products.
        """
        self.products = products

    def add_product(self, product: Product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes a shopping list and calculates the total order cost.
        Each item in shopping_list is a tuple: (Product, quantity).
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price