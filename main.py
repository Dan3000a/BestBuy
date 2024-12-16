from products import Product

def main():
    try:
        bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        mac = Product("MacBook Air M2", price=1450, quantity=100)

        print(bose.buy(50))  # Buy 50 units of Bose, should print total price
        print(mac.buy(100))  # Buy all MacBooks, should print total price
        print(mac.is_active())  # MacBook should now be inactive

        print(bose.show())  # Show details of Bose
        print(mac.show())   # Show details of MacBook

        bose.set_quantity(1000)  # Update quantity for Bose
        print(bose.show())  # Show updated details

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
