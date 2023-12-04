#!/usr/bin/python3
""" prints all City objects from database """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City


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

    # Query the database and print the City objects
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(city)

    session.close()