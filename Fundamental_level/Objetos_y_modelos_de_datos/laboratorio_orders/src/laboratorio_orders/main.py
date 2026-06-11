from laboratorio_orders.models import OrderIn
from laboratorio_orders.mappers import to_entity, to_output

def main():
    data = {
        "id": 1,
        "items": [
            {"name": "Laptop", "price": 1000, "quantity": 1},
            {"name": "Mouse", "price": 50, "quantity": 2}
        ]
    }

    # 🔹 Validación con Pydantic
    order_in = OrderIn(**data)

    # 🔹 Conversión a entidad
    order = to_entity(order_in)

    # 🔹 Lógica de negocio
    print(order)
    print("Total con impuestos:", order.total_with_tax())

    # 🔹 Salida serializable
    order_out = to_output(order)
    print(order_out.model_dump())


if __name__ == "__main__":
    main()