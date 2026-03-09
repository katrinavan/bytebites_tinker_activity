# ByteBites Final UML Design

## Customer
- name: str
- purchase_history: list[Transaction]

## FoodItem
- name: str
- price: float
- category: str
- popularity_rating: int

## Menu
- items: list[FoodItem]

## Transaction
- selected_items: list[FoodItem]

## Relationships
- Customer --> Transaction
- Menu --> FoodItem
- Transaction --> FoodItem