from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.card import CardCreate
from app.models.credit_card import CreditCard
from app.core.security import get_current_user

router = APIRouter(prefix="/cards", tags=["cards"])

@router.post("/")
def create(card: CardCreate, db: Session = Depends(get_db), user_id=Depends(get_current_user)):
    obj = CreditCard(**card.dict(), user_id=user_id)
    db.add(obj)
    db.commit()
    return obj

@router.get("/")
def list_cards(db: Session = Depends(get_db), user_id=Depends(get_current_user)):
    return db.query(CreditCard).filter_by(user_id=user_id).all()