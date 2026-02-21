from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.api import auth, cards, transactions, alerts
from app.models import user, credit_card, transaction, alert

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fintech Enterprise API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(cards.router)
app.include_router(transactions.router)
app.include_router(alerts.router)

@app.get("/health")
def health():
    return {"status":"ok"}