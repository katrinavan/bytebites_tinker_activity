from models import FoodItem, Menu, Transaction


def test_calculate_total_with_multiple_items():
    burger = FoodItem("Spicy Burger", 8.99, "Main", 4.7)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)
    cake = FoodItem("Chocolate Cake", 4.50, "Desserts", 4.6)

    order = Transaction([burger, soda, cake])

    assert order.calculate_total() == 15.98


def test_order_total_is_zero_when_empty():
    order = Transaction()

    assert order.calculate_total() == 0


def test_filter_menu_items_by_category():
    burger = FoodItem("Spicy Burger", 8.99, "Main", 4.7)
    soda = FoodItem("Large Soda", 2.49, "Drinks", 4.1)
    tea = FoodItem("Iced Tea", 2.99, "Drinks", 3.8)

    menu = Menu([burger, soda, tea])
    drinks = menu.filter_by_category("Drinks")

    assert len(drinks) == 2
    assert drinks[0].name == "Large Soda"
    assert drinks[1].name == "Iced Tea"