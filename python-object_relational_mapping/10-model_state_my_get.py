#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa
with a name matching the argument passed
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    state_which_was_given = sys.argv[4]

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (session.query(State).
             filter(State.name == state_which_was_given).
             order_by(State.id).first())

    if state:
        print("{}".format(state.id))
    else:
        print('Not found')

    session.close()
