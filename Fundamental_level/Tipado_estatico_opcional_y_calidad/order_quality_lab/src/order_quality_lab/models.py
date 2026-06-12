from typing import List, Literal, TypedDict

from pydantic import BaseModel, Field


class OrderItemIn(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)


class OrderIn(BaseModel):
    id: int
    items: List[OrderItemIn]
    tax_rate: float = Field(default=0.16, ge=0)


class OrderItemOut(BaseModel):
    name: str
    price: float
    quantity: int
    subtotal: float


class OrderOut(BaseModel):
    id: int
    total: float
    tax: float
    total_with_tax: float
    items: List[OrderItemOut]


# ✅ Tipado avanzado
class PaymentDict(TypedDict):
    method: Literal["cash", "card", "transfer"]
    amount: float