#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
and prevents SQL injections
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """No execution when imported"""

    # Verify that all arguments are presents
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              "<state name searched>".format(sys.argv[0]))
        sys.exit(1)

    # Fetch arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute sql requests and retrieve the results
    cursor = db.cursor()

    # Execute one request to get cities name with there states
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC "
    )
    cursor.execute(query)

    # Fetch the results, prints a list of tuples
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close the cursor and connection to db to free ressources
    cursor.close()
    db.close()
