from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.DTO.advances_DTO import Advance
from api.DTO.comments_DTO import Comment
from api.DTO.expenses_DTO import Expense
from api.DTO.funding_sources_DTO import FundingSource
from api.DTO.proposals_DTO import Proposal
from api.DTO.statuses_DTO import Status
from api.DTO.units_DTO import Unit
from api.DTO.users_DTO import User

from database_secrets import DB_VPN_URL, DB_LOGIN, DB_PASSWORD, DB_NAME


if __name__ == '__main__':
    engine = create_engine(f"postgresql://{DB_LOGIN}:{DB_PASSWORD}@{DB_VPN_URL}/{DB_NAME}",
                           echo=False)  # echo is for debug
    Session = sessionmaker(engine)
    session = Session()

    # users = session.query(User)  # API query
    proposals = session.query(Proposal)
    pass
    # for user in users:
    #     print(f"{user.name} {user.surname}")
    #
    # users = session.execute("SELECT * FROM users")  # Normal SQL query (not recommended)
    # for user in users:
    #     print(f"{user[1]} {user[2]}")

