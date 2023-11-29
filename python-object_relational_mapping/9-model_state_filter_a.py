#!/usr/bin/python3
""" lists all State objects that contain the letter 'a' from database """
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

    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()
