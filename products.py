class Product:
    """
    Represents a product with name, price, and quantity.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a product with a name, price, and quantity.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid name, price, or quantity.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets a new quantity and deactivates if quantity is 0."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns the product details as a string."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a specified quantity of the product and updates the stock.
        Returns the total price.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock to fulfill the order.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity
