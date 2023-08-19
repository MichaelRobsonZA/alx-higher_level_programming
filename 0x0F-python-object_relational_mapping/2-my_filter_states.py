#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa
using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Set up the connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the database for cities and their corresponding states
    cities_and_states = session.query(City, State).\
                        filter(City.state_id == State.id).order_by(City.id).all()

    # Print the results
    for city, state in cities_and_states:
        print("{}: ({}) {}".format(city.name, state.id, state.name))

    # Close the session
    session.close()
