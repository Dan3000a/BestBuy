from products import Product
from store import Store


def start(store: Store):
    """
    Runs the user interface for the store.
    Displays a menu and allows the user to interact with the store.
    """
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\n------")
            for idx, product in enumerate(store.get_all_products(), start=1):
                print(f"{idx}. {product.show()}")
            print("------")
        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"Total of {total_quantity} items in store")
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def make_order(store: Store):
    """
    Handles the process of making an order.
    Prompts the user to select products and quantities.
    """
    print("\n------")
    products = store.get_all_products()
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.show()}")
    print("------")

    shopping_list = []

    while True:
        product_choice = input("Which product # do you want? (Enter empty text to finish): ")
        if product_choice == "":
            break

        try:
            product_index = int(product_choice) - 1
            if product_index < 0 or product_index >= len(products):
                print("Invalid product number. Please try again.")
                continue

            product = products[product_index]
            quantity = input("What amount do you want? ")
            if not quantity.isdigit():
                print("Invalid quantity. Please enter a positive number.")
                continue

            shopping_list.append((product, int(quantity)))
            print("Product added to list!")

        except ValueError:
            print("Invalid input. Please try again.")

    try:
        total_price = store.order(shopping_list)
        print(f"Order made! Total payment: ${total_price}")
    except ValueError as error:
        print(f"Error while making order: {error}")


def main():
    """
    Sets up the inventory and runs the user interface.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()