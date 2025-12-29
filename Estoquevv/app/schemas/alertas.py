from pydantic import BaseModel


class Alert(BaseModel):
    sku: str
    store: str
    message: str
