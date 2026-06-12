from typing import List

from order_quality_lab.entities import Order, OrderItem
from order_quality_lab.models import OrderIn, OrderItemOut, OrderOut


def to_entity(order_in: OrderIn) -> Order:
    items: List[OrderItem] = [
        OrderItem(
            name=i.name,
            price=i.price,
            quantity=i.quantity,
        )
        for i in order_in.items
    ]

    return Order(
        id=order_in.id,
        items=items,
        tax_rate=order_in.tax_rate,
    )


def to_output(order: Order) -> OrderOut:
    return OrderOut(
        id=order.id,
        total=order.total(),
        tax=order.tax(),
        total_with_tax=order.total_with_tax(),
        items=[
            OrderItemOut(
                name=i.name,
                price=i.price,
                quantity=i.quantity,
                subtotal=i.subtotal(),
            )
            for i in order.items
        ],
    )