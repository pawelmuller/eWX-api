from api.utils.db_connection import db_connect
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from api.DTO import *


def get_expenses() -> list:
    with db_connect() as session:
        expenses = session.query(Expense).all()
    return expenses


def get_expense(expense_id: int) -> Expense:
    with db_connect() as session:
        expense = session.query(Expense).where(Expense.expense_id == expense_id).first()
    return expense


def create_expense(name: str,
                   quantity: int,
                   price: int,
                   expense_type: str,
                   proposal_id: int) -> (int, str):
    with db_connect() as session:
        new_id = session.query(func.max(Expense.expense_id)).scalar() + 1
        new_expense = Expense(expense_id=new_id,
                              name=name,
                              quantity=quantity,
                              price=price,
                              type=expense_type,
                              proposal_id=proposal_id)
        session.add(new_expense)
        try:
            session.commit()
        except SQLAlchemyError as error:
            return None, str(error.__dict__['orig'])
    return new_id, None
