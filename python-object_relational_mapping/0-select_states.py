#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password and database name.
"""

import MySQLdb  # To communicate with MySQL
import sys  # Pour récupérer les arguments passés au script


if __name__ == "__main__":
    """No execution when imported"""

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",  # MySQL server adress (local here)
        port=3306,  # MySQL default port
        # Parameters
        user=username,
        passwd=password,
        db=db_name
    )

# Create a cursor object to execute sql requests and retrieve the results
cursor = db.cursor()

# Execute the query to get all states sorted by id in ascending order
cursor.execute("SELECT * FROM states ORDER BY id ASC;")

# Fetch the results, prints a list of tuples (each row in a line in the table)
rows = cursor.fetchall()
for row in rows:
    print(row)

# Once done, close cursor and connection to db to free ressources
cursor.close()
db.close()
