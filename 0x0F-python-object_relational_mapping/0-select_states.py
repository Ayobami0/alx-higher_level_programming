<<<<<<< HEAD
#!./venv/bin/python3
"""A module for database connectivity"""
=======
#!/usr/bin/python3

import MySQLdb
>>>>>>> parent of 0389d06 (fix: checker fix for task 0)
import sys
MySQLdb = __import__('MySQLdb')
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

for row in rows:
    print(row)
