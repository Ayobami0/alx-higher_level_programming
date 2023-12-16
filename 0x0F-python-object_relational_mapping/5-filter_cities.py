#!/usr/bin/python3
"""
A module for database connectivity. This a just a minor script.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    mysql_user, mysql_pass, db_name, state_name = args
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
            SELECT cities.name
            FROM cities
            WHERE state_id = (SELECT id FROM states WHERE name = %s)
        """,
        (state_name,),
    )

    rows = c.fetchall()

    for row_idx in range(len(rows)):
        if row_idx != len(rows) - 1:
            print(rows[row_idx][0], end=", ")
        else:
            print(rows[row_idx][0], end="\n")
