# ByteBites Final UML Design

## Customer
**Attributes**
- name: str
- purchase_history: list[Transaction]

**Methods**
- add_transaction(transaction: Transaction) -> None

## FoodItem
**Attributes**
- name: str
- price: float
- category: str
- popularity_rating: int

## Menu
**Attributes**
- items: list[FoodItem]

**Methods**
- add_item(item: FoodItem) -> None
- filter_by_category(category: str) -> list[FoodItem]

## Transaction
**Attributes**
- selected_items: list[FoodItem]

**Methods**
- add_item(item: FoodItem) -> None
- calculate_total() -> float

## Relationships
- Customer 1 --> * Transaction
- Menu 1 --> * FoodItem
- Transaction 1 --> * FoodItem