#!/usr/bin/python3
"""Updates the name of a state in the database"""

from db_session import get_session
from model_state import State

if __name__ == "__main__":
    # State ID to update (change this to the actual state ID)
    state_id = 1

    # New name for the state
    new_name = "Updated State Name"

    # Get a session
    session = get_session()

    try:
        # Retrieve the state from the database
        state = session.query(State).get(state_id)

        if state:
            # Update the state's name
            state.name = new_name

            # Commit the transaction
            session.commit()
            print(f"Updated state name. New name: {state.name}")
        else:
            print(f"State with ID {state_id} not found.")
    except Exception as e:
        # Roll back the transaction in case of an error
        session.rollback()
        print(f"Error: {e}")
    finally:
        # Close the session
        session.close()
