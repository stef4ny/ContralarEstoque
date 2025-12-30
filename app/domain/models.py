from pydantic import BaseModel


class SKU(BaseModel): #SKU é Item de Estoque
    sku: str
    name: str | None = None


class Loja(BaseModel):
    code: str
    name: str | None = None


class Estoque(BaseModel):
    sku: str
    store: str
    quantity: int
