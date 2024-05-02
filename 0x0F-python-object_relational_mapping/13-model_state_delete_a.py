#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the
database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username, password, database = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()

    states_contains_a = session.query(State).filter(State.name.like('%a%'))

    for state in states_contains_a:
        session.delete(state)
    session.commit()