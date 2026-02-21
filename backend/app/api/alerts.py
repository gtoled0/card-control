from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.alert import Alert
from app.core.security import get_current_user

router = APIRouter(prefix="/alerts", tags=["alerts"])

@router.get("/")
def list_alerts(db: Session = Depends(get_db), user_id=Depends(get_current_user)):
    return db.query(Alert).filter_by(user_id=user_id).all()