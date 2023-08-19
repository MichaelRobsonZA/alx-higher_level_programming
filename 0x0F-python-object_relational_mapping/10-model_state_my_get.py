#!/usr/bin/python3
"""Adds a new city to the database"""

from db_session import get_session
from model_city import City

if __name__ == "__main__":
    # City details
    city_name = "New City"
    state_id = 1  # ID of the state to associate the city with

    # Get a session
    session = get_session()

    try:
        # Create a new City object
        new_city = City(name=city_name, state_id=state_id)

        # Add the city to the database
        session.add(new_city)
        session.commit()
        print(f"Added new city: {new_city.name} (ID: {new_city.id})")
    except Exception as e:
        # Roll back the transaction in case of an error
        session.rollback()
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
