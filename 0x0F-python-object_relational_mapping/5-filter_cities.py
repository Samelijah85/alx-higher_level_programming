#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database,
        charset="utf8",
    )
    cursor = db.cursor()
    query = """SELECT cities.name FROM cities INNER JOIN states ON
     states.id=cities.state_id WHERE states.name=%s ORDER BY cities.id"""
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    cities = [row[0] for row in results]
    print(*cities, sep=", ")
    cursor.close()
    db.close()
