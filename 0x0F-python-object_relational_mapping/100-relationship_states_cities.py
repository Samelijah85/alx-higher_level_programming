#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username, password, database = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name="California")
    session.add(california)
    san_francisco = City(name="San Francisco", state=california)
    session.add(san_francisco)
    session.commit()
