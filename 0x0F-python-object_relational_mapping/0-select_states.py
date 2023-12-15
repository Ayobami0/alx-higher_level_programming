#!/usr/bin/python3
"""A module for database connectivity"""
import MySQLdb
import sys

args = sys.argv[1:]
mysql_user, mysql_pass, db_name = args
db = MySQLdb.connect(
    host="localhost",
    user=mysql_user,
    password=mysql_pass,
    port=3306,
    database=db_name,
)

db.query(
    """
SELECT * FROM states ORDER BY id
"""
)

rows = db.store_result().fetch_row(maxrows=0)

if __name__ == "__main__":
    for row in rows:
        print(row)
