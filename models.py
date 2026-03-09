# ByteBites class scaffolds
# Customer stores a customer's name and purchase history.
# FoodItem stores the name, price, category, and popularity rating of one item.
# Menu stores the full collection of food items.
# Transaction stores selected items for one transaction.

class Customer:
    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history if purchase_history is not None else []

    def add_transaction(self, transaction):
        self.purchase_history.append(transaction)


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, item):
        self.items.append(item)


class Transaction:
    def __init__(self, selected_items=None):
        self.selected_items = selected_items if selected_items is not None else []

    def add_item(self, item):
        self.selected_items.append(item)


if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 8.99, "Main", 4.7)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)

    menu = Menu([burger, soda])
    order = Transaction([burger])
    customer = Customer("Katrina", [order])

    print(customer.name)
    print(burger.name, burger.price, burger.category, burger.popularity_rating)
    print(len(menu.items))
    print(len(order.selected_items))