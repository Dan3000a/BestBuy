from products import Product
from store import Store

def main():
    # Step 1: Create a list of products
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]

    # Step 2: Initialize the store with the list of products
    store = Store(product_list)

    # Step 3: Retrieve all active products
    products = store.get_all_products()

    # Step 4: Print the total quantity of products in the store
    print("Total quantity in store:", store.get_total_quantity())

    # Step 5: Place an order for some products and print the total cost
    total_cost = store.order([
        (products[0], 1),  # Buy 1 MacBook Air M2
        (products[1], 2)   # Buy 2 Bose QuietComfort Earbuds
    ])
    print(f"Total cost of the order: ${total_cost}")

if __name__ == "__main__":
    main()