# ByteBites class scaffolds and methods
# Customer stores a customer's name and purchase history.
# FoodItem stores the name, price, category, and popularity rating of one item.
# Menu stores the full collection of food items and supports filtering/sorting.
# Transaction stores selected items for one transaction and computes totals.


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

    def filter_by_category(self, category):
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    def __init__(self, selected_items=None):
        self.selected_items = selected_items if selected_items is not None else []

    def add_item(self, item):
        self.selected_items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.selected_items)


if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 8.99, "Main", 4.7)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)
    cake = FoodItem("Chocolate Cake", 4.50, "Desserts", 4.6)
    tea = FoodItem("Iced Tea", 2.99, "Drinks", 3.8)

    menu = Menu([burger, soda, cake, tea])

    print("Drinks:")
    for item in menu.filter_by_category("Drinks"):
        print(item.name)

    print("\nSorted by popularity:")
    for item in menu.sort_by_popularity():
        print(item.name, item.popularity_rating)

    order = Transaction([burger, soda, cake])
    print("\nOrder total:")
    print(order.calculate_total())