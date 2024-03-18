#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database
hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker

if __name__ == '__main__':
    username, password, database, state_name = sys.argv[1:5]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    session = scoped_session(
        sessionmaker(
            bind=engine
        )
    )

    searched_state = session.query(State).filter_by(name=state_name).first()

    if searched_state:
        print(searched_state.id)
    else:
        print('Not found')
