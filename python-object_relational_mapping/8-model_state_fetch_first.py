#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa
in ascending order by states.id
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if not state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
