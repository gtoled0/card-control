from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.transaction import TransactionCreate
from app.models.transaction import Transaction
from app.services.alert_service import check_alerts
from app.core.security import get_current_user

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/")
def create(tx: TransactionCreate, db: Session = Depends(get_db), user_id=Depends(get_current_user)):
    obj = Transaction(**tx.dict(), user_id=user_id)
    db.add(obj)
    db.commit()
    check_alerts(db, tx.card_id, user_id)
    return obj