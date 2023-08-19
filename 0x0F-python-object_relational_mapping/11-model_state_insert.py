#!/usr/bin/python3
"""Queries and displays cities in a specific state from the database"""

from db_session import get_session
from model_city import City

if __name__ == "__main__":
    # State ID to query cities for (change this to the actual state ID)
    state_id = 1

    # Get a session
    session = get_session()

    try:
        # Query cities for the specified state
        cities = session.query(City).filter_by(state_id=state_id).all()

        if cities:
            print(f"Cities in State ID {state_id}:")
            for city in cities:
                print(f"- {city.name} (ID: {city.id})")
        else:
            print(f"No cities found for State ID {state_id}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
