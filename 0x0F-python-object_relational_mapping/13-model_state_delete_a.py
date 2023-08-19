#!/usr/bin/python3
"""Counts the number of cities in the database"""

from db_session import get_session
from model_city import City

if __name__ == "__main__":
    # Get a session
    session = get_session()

    try:
        # Query the total number of cities
        city_count = session.query(City).count()
        print(f"Total number of cities: {city_count}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
