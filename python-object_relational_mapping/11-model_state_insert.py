#!/usr/bin/python3
"""
First ORM
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

    louis = State(name='Louisiana')
    session.add(louis)
    session.commit()

    # states = session.query(State).order_by(State.id).all()
    print('{}'.format(louis.id))
    # for state in states:
    #    print("{}: {}".format(state.id, state.name))

    session.close()
