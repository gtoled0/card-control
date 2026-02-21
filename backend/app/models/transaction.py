from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    date = Column(DateTime, default=datetime.utcnow)
    card_id = Column(Integer, ForeignKey("credit_cards.id"))
    user_id = Column(Integer, ForeignKey("users.id"))