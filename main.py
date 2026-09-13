from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from Backend.financial_Info import FinancialData
from Backend.user_Info import User

app = FastAPI()
financial_db = FinancialData()
user_info = User()

class UserSchema(BaseModel):
    name: str
    country: str

class TransactionSchema(BaseModel):
    type: str
    amount: float
    description: str

@app.post("/transactions/add")
def add_transaction(transaction: TransactionSchema):
    if transaction.type not in ["Income", "Outcome"]:
        raise HTTPException(status_code=400, detail="Error, transaction type invalid. Must be 'Income' or 'Outcome'")
    if transaction.amount <= 0:
        raise HTTPException(status_code=400, detail="Error, transaction amount must be a positive number")
    new_transaction = [transaction.type, transaction.amount, transaction.description]
    financial_db.add_dataframe(new_transaction)
    return {"message": "Transaction added successfully", "transaction": new_transaction}

@app.get("/transactions/calculate")
def calculate_transactions():
    if financial_db.df.empty:
        raise HTTPException(status_code=400, detail="No data to calculate..")
    financial_db.calculate_data()
    return {
        "Total Income": financial_db.income,
        "Total Outcome": financial_db.outcome,
        "Balance": financial_db.total
    }

@app.get("/transactions/print")
def print_transactions():
    if financial_db.df.empty:
        raise HTTPException(status_code=400, detail="No data to print..")
    dataFrame_string = financial_db.df.to_string(index=False)
    return {"transactions": dataFrame_string}

@app.post("/user/info")
def get_user_info(user: UserSchema):
    if not user.name or not user.country:
        raise HTTPException(status_code=400, detail="Error, user name and country cannot be empty")
    user_info.name = user.name
    user_info.country = user.country
    return {"message": "User information saved successfully", "user": {"name": user_info.name, "country": user_info.country}}

@app.post("/ia/ask")
def ai_chat(prompt: str):
    if not prompt:
        raise HTTPException(status_code=400, detail="Error, prompt cannot be empty")