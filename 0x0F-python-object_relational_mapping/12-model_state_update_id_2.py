#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
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

    state_to_update = session \
        .query(State) \
        .filter_by(id=2) \
        .update({"name": "New Mexico"})
    session.commit()
