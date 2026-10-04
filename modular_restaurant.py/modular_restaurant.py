MENU = {
    1: {"name": "Burger", "price": 50.00},
    2: {"name": "Fries", "price": 30.00},
    3: {"name": "Fried Chicken", "price": 80.00},
    4: {"name": "Spaghetti", "price": 60.00},
    5: {"name": "Soda", "price": 25.00}
}

DISCOUNT_RATE = 0.10


def display_welcome_message():
    print("\n" + "*" * 40)
    print(f"{'WELCOME TO FAST FOOD EXPRESS':^40}")
    print("*" * 40)


def display_exit_message():
    print("\nThank you for visiting! Have a great day!")


def display_menu():
    print("\n" + "=" * 40)
    print(f"{'FAST FOOD MENU':^40}")
    print("=" * 40)
    print(f"{'Item #':<8}{'Item Name':<22}{'Price':>10}")
    print("-" * 40)

    for item_id, details in MENU.items():
        print(f"{item_id:<8}{details['name']:<22}P{details['price']:>9.2f}")

    print("=" * 40)


def get_item_choice():
    while True:
        try:
            item_choice = int(
                input("\nEnter the Item Number you want to order: ")
            )

            if item_choice in MENU:
                return item_choice

            print("Invalid item number! Please pick an item from the menu.")

        except ValueError:
            print("Invalid input! Please enter a valid numerical Item Number.")


def get_quantity(item_name):
    while True:
        try:
            quantity = int(input(f"Enter quantity for {item_name}: "))

            if quantity > 0:
                return quantity

            print("Quantity must be at least 1.")

        except ValueError:
            print("Invalid input! Quantity must be a whole number.")


def add_order(order_list, item_choice, quantity):
    item_data = MENU[item_choice]
    item_total = item_data["price"] * quantity

    order_list.append({
        "name": item_data["name"],
        "price": item_data["price"],
        "quantity": quantity,
        "item_total": item_total
    })

    print(f"Added {quantity}x {item_data['name']} to your order.")


def ask_for_another_item():
    while True:
        another = input(
            "\nWould you like to order another item? (yes/no): "
        ).strip().lower()

        if another in ["yes", "y", "no", "n"]:
            return another

        print("Invalid response. Please enter 'yes' or 'no'.")


def calculate_order_totals(order_list):
    subtotal = 0.0

    for item in order_list:
        subtotal += item["item_total"]

    if subtotal >= 200:
        discount = subtotal * DISCOUNT_RATE
    else:
        discount = 0.0

    grand_total = subtotal - discount

    return subtotal, discount, grand_total


def print_receipt(order_list):
    subtotal, discount, grand_total = calculate_order_totals(order_list)

    print("\n" + "=" * 45)
    print(f"{'FAST FOOD EXPRESS RECEIPT':^45}")
    print(f"{'Official Order Summary':^45}")
    print("=" * 45)
    print(f"{'Item':<18}{'Qty':<6}{'Price':<10}{'Total':>11}")
    print("-" * 45)

    for order in order_list:
        print(
            f"{order['name']:<18}"
            f"{order['quantity']:<6}"
            f"P{order['price']:<9.2f}"
            f"P{order['item_total']:>10.2f}"
        )

    print("-" * 45)
    print(f"{'Subtotal:':<34}P{subtotal:>9.2f}")

    if discount > 0:
        print(
            f"{'Discount (10% over P200):':<34}"
            f"-P{discount:>8.2f}"
        )

    print(f"{'GRAND TOTAL:':<34}P{grand_total:>9.2f}")
    print("=" * 45)
    print(f"{'Thank you for dining with us!':^45}")
    print("=" * 45 + "\n")


def run_ordering_system():
    display_welcome_message()

    while True:
        user_choice = input(
            "Would you like to place an order? (yes/no): "
        ).strip().lower()

        if user_choice in ["yes", "y"]:
            break

        elif user_choice in ["no", "n"]:
            display_exit_message()
            return

        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

    order_list = []

    while True:
        display_menu()

        item_choice = get_item_choice()
        quantity = get_quantity(MENU[item_choice]["name"])

        add_order(order_list, item_choice, quantity)

        another = ask_for_another_item()

        if another in ["no", "n"]:
            break

    if order_list:
        print_receipt(order_list)


if __name__ == "__main__":
    run_ordering_system()

