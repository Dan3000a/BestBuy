class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes the product with name, price, and quantity.
        Active is set to True by default.
        Raises an exception for invalid input.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid name, price, or quantity.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Default to active

    def get_quantity(self) -> float:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets the product quantity.
        If quantity is 0, deactivates the product.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self) -> str:
        """Returns a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Processes a purchase of a given quantity.
        Returns the total cost.
        Raises an exception if quantity is invalid or exceeds stock.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock to fulfill the order.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity