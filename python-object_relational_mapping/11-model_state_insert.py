#!/usr/bin/python3
""" adds State object to database """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # set up connection to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)
    # create a session and db tables if needed
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    # create session instance
    session = Session()
    # create new state object
    new_state = State(name="Louisiana")
    # add new state object to session and commit to db
    session.add(new_state)
    session.commit
    # get State object from bd to ensure id is populated
    new_state = session.query(State).filter_by(name="Louisiana").first()

    print(new_state.id)

    session.close()
