#!/usr/bin/python3
"""
This module perform some actions on the sql database using sqlalchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    args = sys.argv[1:]
    mysql_user, mysql_pass, db_name = args
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            mysql_user,
            mysql_pass,
            db_name,
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(
            session.query(State).filter(State.id == city.state_id).one().name,
            city.id, city.name))
    session.close()
