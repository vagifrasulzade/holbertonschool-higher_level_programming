#!/usr/bin/python3
"""
First ORM
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = (session.query(State, City).
                     join(City, State.id == City.state_id).
                     order_by(City.id).all())

    for state, city in states_cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
