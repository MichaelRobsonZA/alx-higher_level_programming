#!/usr/bin/python3
"""Updates the name of a city in the database"""

from db_session import get_session
from model_city import City

if __name__ == "__main__":
    # City ID and new name (change these to the actual city ID and new name)
    city_id = 1
    new_city_name = "Updated City Name"

    # Get a session
    session = get_session()

    try:
        # Retrieve the city from the database
        city = session.query(City).get(city_id)

        if city:
            # Update the city's name
            city.name = new_city_name
            session.commit()
            print(f"Updated city name (ID: {city.id}): {city.name}")
        else:
            print(f"City with ID {city_id} not found.")
    except Exception as e:
        # Roll back the transaction in case of an error
        session.rollback()
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
