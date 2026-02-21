from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    card_id: int