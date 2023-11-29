#!/usr/bin/python3
""" prints the State object with the name passed as argument from database """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_passed = sys.argv[4]
    # set up connection to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)
    # create a session and db tables if needed
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    # create session instance
    session = Session()

    state = session.query(State).filter(State.name == name_passed).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
