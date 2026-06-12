from order_quality_lab.mappers import to_entity, to_output
from order_quality_lab.models import OrderIn, OrderItemIn


def main() -> None:
    order_in = OrderIn(
        id=1,
        items=[
            OrderItemIn(name="Laptop", price=1000, quantity=1),
            OrderItemIn(name="Mouse", price=50, quantity=2),
        ],
    )

    order = to_entity(order_in)

    print(order)
    print(order.total_with_tax())

    output = to_output(order)
    print(output.model_dump())


if __name__ == "__main__":
    main()