#!/usr/bin/python3
"""Adds a new state to the database"""

from db_session import get_session
from model_state import State

if __name__ == "__main__":
    # Create a new state object
    new_state = State(name='New State')

    # Get a session
    session = get_session()

    try:
        # Add the new state to the session
        session.add(new_state)

        # Commit the transaction
        session.commit()
        print(f"Added new state with ID: {new_state.id}")
    except Exception as e:
        # Roll back the transaction in case of an error
        session.rollback()
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
