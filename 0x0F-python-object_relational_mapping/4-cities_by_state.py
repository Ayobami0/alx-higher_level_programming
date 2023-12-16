#!/usr/bin/python3
"""
A module for database connectivity. This a just a minor script.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    mysql_user, mysql_pass, db_name = args
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_user,
        password=mysql_pass,
        port=3306,
        database=db_name,
    )
    c = db.cursor()
    c.execute(
        """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    """,
    )

    rows = c.fetchall()

    for row in rows:
        print(row)
