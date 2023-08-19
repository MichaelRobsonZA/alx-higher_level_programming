#!/usr/bin/python3
"""Lists all cities from the DB hbtn_0e_4_usa using SQLAlchemy"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).filter
    (City.state_id == State.id).order_by(City.id).all()

    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
