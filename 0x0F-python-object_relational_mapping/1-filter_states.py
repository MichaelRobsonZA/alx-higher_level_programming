#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N) from the DB
hbtn_0e_0_usa using SQLAlchemy"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%N%')).order_by
    (State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
