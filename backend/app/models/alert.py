from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    message = Column(String)
    level = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))