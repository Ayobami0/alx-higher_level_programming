#!/usr/bin/python3
"""
This module perform some actions on the sql database using sqlalchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    args = sys.argv[1:]
    mysql_user, mysql_pass, db_name, st_name = args
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

    s = session.query(State).filter(State.name == st_name).one_or_none()

    if s is not None:
        print(s.id)
    else:
        print("Not found")
    session.close()
