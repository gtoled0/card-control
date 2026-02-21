from sqlalchemy.orm import Session
from app.models.alert import Alert
from app.models.credit_card import CreditCard
from app.services.invoice_service import invoice_total

THRESHOLD = 0.8

def check_alerts(db: Session, card_id: int, user_id: int):
    card = db.query(CreditCard).filter_by(id=card_id, user_id=user_id).first()
    total = invoice_total(db, card_id)
    usage = total / card.limit_amount

    if usage >= 1:
        db.add(Alert(message="Limite ultrapassado", level="critical", user_id=user_id))
    elif usage >= THRESHOLD:
        db.add(Alert(message="80% do limite atingido", level="warning", user_id=user_id))

    db.commit()