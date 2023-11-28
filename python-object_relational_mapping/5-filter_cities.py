#!/usr/bin/python3
""" takes name of a state as argument and lists all cities of state from db """
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # Create a cursor object to execute queries
    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name \
             FROM states, cities WHERE cities.state_id = states.id \
             AND states.name = %s ORDER BY cities.id ASC"
    search = sys.argv[4],
    cursor.execute(query, search)
    cities = cursor.fetchall()
    cities = ", ".join([city[1] for city in cities])
    print(cities)
    cursor.close()
    db.close()
