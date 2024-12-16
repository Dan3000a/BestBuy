
# BestBuy Tech Equipment Store Engine

Welcome to the **BestBuy Tech Equipment Store Engine** repository! This Python-based project provides the functionality for managing a tech equipment store like "Best Buy." With this engine, you can list products, manage inventory, and place orders seamlessly. 💻✨

---

## Demo 📺

The store operates with a simple and user-friendly menu interface:

```
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```

### Example Usage:

1. **List Products**:
   ```
   1. MacBook Air M2, Price: $1450, Quantity: 100
   2. Bose QuietComfort Earbuds, Price: $250, Quantity: 500
   3. Google Pixel 7, Price: $500, Quantity: 250
   ```

2. **Total Items in Store**:
   ```
   Total of 850 items in store
   ```

3. **Make an Order**:
   ```
   Which product # do you want? 1
   What amount do you want? 50
   Product added to list!

   Order made! Total payment: $72500
   ```

4. **Quit the Application**.

---

## Features ✨

1. **Product Management**:
   - Add or remove products.
   - Manage product quantities and status.
   - Activate or deactivate products automatically based on inventory.

2. **Store Management**:
   - Maintain a list of active products.
   - Check the total inventory quantity.
   - Process multiple orders in one transaction.

3. **User Interface**:
   - Simple and intuitive command-line interface.
   - Handle edge cases such as invalid inputs or out-of-stock items gracefully.

---

## Project Structure 📂

- `main.py`: Entry point for the application. Manages the user interface.
- `products.py`: Contains the `Product` class for handling individual product details.
- `store.py`: Contains the `Store` class for managing product collections and order processing.

---

## Getting Started 🚀

### Prerequisites

- Python 3.7 or later
- Git for version control

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourname/bestbuy.git
   cd bestbuy
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

---

## Classes and Methods

### **Product Class**
Represents individual products in the store.

- **Attributes**:
  - `name`: Name of the product.
  - `price`: Price of the product.
  - `quantity`: Available stock.
  - `active`: Active status of the product.

- **Key Methods**:
  - `buy(quantity)`: Handles product purchase and updates stock.
  - `show()`: Displays product details.
  - `activate()/deactivate()`: Toggles the active status.

### **Store Class**
Handles a collection of products and order management.

- **Attributes**:
  - `products`: List of active `Product` instances.

- **Key Methods**:
  - `add_product(product)`: Adds a product to the store.
  - `remove_product(product)`: Removes a product from the store.
  - `get_total_quantity()`: Returns the total inventory.
  - `order(shopping_list)`: Processes multiple product orders.

---

## Development Workflow 🛠️

1. **Initialize Git Repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourname/bestbuy.git
   git push -u origin main
   ```

2. **Regular Commits**:
   - Commit after implementing each feature:
     ```bash
     git add .
     git commit -m "Implemented [feature]"
     git push
     ```

3. **Clone for Deployment**:
   - Clone the repository to Codio or another environment to ensure all functionality works as expected.

---

## Testing and Edge Cases 🧪

- Test ordering a quantity larger than available stock.
- Verify behavior when a product runs out of stock.
- Check for invalid parameters during product creation.

---

## Why Use Git and GitHub? 🌐

1. **Version Control**: Maintain a clear history of changes.
2. **Portfolio Building**: Showcase your work to potential employers.
3. **Deployment Preparation**: Learn real-world practices for managing and deploying code.

---

## Contribution 🤝

Contributions are welcome! Please open an issue or submit a pull request with detailed comments.

---

## License 📜

This project is licensed under the [BSD3 License](LICENSE).

---

Happy Coding! 🚀💻
