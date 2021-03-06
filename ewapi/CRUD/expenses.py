from ewapi.utils.db_connection import get_session, get_next_id
from ewapi.DTO import *


def get_expenses() -> list:
    with get_session() as session:
        expenses = session.query(Expense).all()
    return expenses


def get_expense(expense_id: int) -> Expense:
    with get_session() as session:
        expense = session.query(Expense).where(Expense.expense_id == expense_id).first()
    return expense


def create_expense(session,
                   name: str,
                   quantity: int,
                   price: int,
                   expense_type: str,
                   proposal_id: int) -> int:
    new_id = get_next_id(session, Expense.expense_id)
    new_expense = Expense(expense_id=new_id,
                          name=name,
                          quantity=quantity,
                          price=price,
                          type=expense_type,
                          proposal_id=proposal_id)
    session.add(new_expense)
    return new_id
