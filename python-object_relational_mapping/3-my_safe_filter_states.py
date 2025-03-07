#!/usr/bin/python3
"""
This script lists all states corresponding to a
given argument and prevents SQL injections
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
        host="localhost", user=mysql_user, passwd=mysql_password, db=db_name)

    # Create a cursor object to execute sql requests and retrieve the results
    cursor = db.cursor()

    # Use a parametered request to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch the results, prints a list of tuples
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection to db to free ressources
    cursor.close()
    db.close()
