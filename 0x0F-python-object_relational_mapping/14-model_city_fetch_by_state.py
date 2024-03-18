#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker

if __name__ == '__main__':
    username, password, database = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    cities_and_states = (
        session.query(State.name, City.id, City.name)
        .filter(State.id == City.state_id)
        .order_by(City.id)
    )

    for state, city_id, city_name in cities_and_states:
        print("{}: ({}) {}".format(state, city_id, city_name))
