#!/usr/bin/python3
"""Deletes a state from the database"""

from db_session import get_session
from model_state import State

if __name__ == "__main__":
    # State ID to delete (change this to the actual state ID)
    state_id = 1

    # Get a session
    session = get_session()

    try:
        # Retrieve the state from the database
        state = session.query(State).get(state_id)

        if state:
            # Delete the state
            session.delete(state)
            session.commit()
            print(f"Deleted state with ID {state_id}")
        else:
            print(f"State with ID {state_id} not found.")
    except Exception as e:
        # Roll back the transaction in case of an error
        session.rollback()
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
