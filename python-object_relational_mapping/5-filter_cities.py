#!/usr/bin/python3
"""
This script lists all cities of a given state
from the database hbtn_0e_4_usa
and prevents SQL injections
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """No execution when imported"""

    # Verify that all arguments are presents
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              "<state name searched>".format(sys.argv[0]))
        sys.exit(1)

    # Fetch arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create a cursor object to execute sql requests and retrieve the results
    cursor = db.cursor()

    # Execute one request to get cities name of the given state
    query = (
    "SELECT cities.name "
    "FROM cities "
    "JOIN states ON cities.state_id = states.id "
    "WHERE states.name = %s "
    "ORDER BY cities.id ASC "
    )
    cursor.execute(query, (state_name,))

    # Fetch the results, prints a list separated by comas
    results = cursor.fetchall()
    city_names = ",".join(row[0] for row in results)
    print(city_names)

    # Close the cursor and connection to db to free ressources
    cursor.close()
    db.close()
