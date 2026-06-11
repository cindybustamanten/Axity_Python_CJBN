from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class OrderItem:
    name: str
    price: float
    quantity: int

    def subtotal(self) -> float:
        return self.price * self.quantity


@dataclass(order=True)
class Order:
    id: int
    items: List[OrderItem] = field(default_factory=list)
    tax_rate: float = 0.16

    def total(self) -> float:
        return sum(item.subtotal() for item in self.items)

    def tax(self) -> float:
        return self.total() * self.tax_rate

    def total_with_tax(self) -> float:
        return self.total() + self.tax()

    # Dunder method
    def __str__(self):
        return f"Order(id={self.id}, total={self.total_with_tax():.2f})"

    # Ejemplo operator overloading
    def __add__(self, other: "Order") -> "Order":
        return Order(
            id=max(self.id, other.id) + 1,
            items=self.items + other.items,
            tax_rate=self.tax_rate
        )