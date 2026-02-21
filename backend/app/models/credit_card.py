from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.core.database import Base

class CreditCard(Base):
    __tablename__ = "credit_cards"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    limit_amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))