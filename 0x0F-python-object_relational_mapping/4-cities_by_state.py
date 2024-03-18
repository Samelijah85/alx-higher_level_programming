#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database,
        charset="utf8",
    )
    cursor = db.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities
     INNER JOIN states ON states.id=cities.state_id ORDER BY cities.id"""
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
