from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.transaction import Transaction

def invoice_total(db: Session, card_id: int):
    return db.query(func.coalesce(func.sum(Transaction.amount),0)).filter(Transaction.card_id==card_id).scalar()