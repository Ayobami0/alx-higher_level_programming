#!/usr/bin/python3
"""
This module perform some actions on the sql database using sqlalchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

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

    session.add(State(name="California"))
    session.add(
        City(
            name="San Francisco",
            state_id=session.query(State).filter_by(name="California").first(),
        )
    )
    session.commit()
    session.close()
