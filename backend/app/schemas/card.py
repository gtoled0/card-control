from pydantic import BaseModel

class CardCreate(BaseModel):
    name: str
    limit_amount: float