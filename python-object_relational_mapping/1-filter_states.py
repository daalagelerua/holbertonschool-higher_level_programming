#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb  # To communicate with MySQL


if __name__ == "__main__":
    """No execution when imported"""

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",  # MySQL server adress (local here)
        port=3306,  # MySQL default port
        # Parameters
        user=sys.argv[1],   # User name
        passwd=sys.argv[2],  # Password
        db=sys.argv[3]       # Database name
    )

# Create a cursor object to execute sql requests and retrieve the results
cursor = db.cursor()

# Execute the query to get all states with name starting by 'N'
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

# Fetch the results prints a list of tuples (each state is a line in the table)
states = cursor.fetchall()
for state in states:
    print(state)

# Once done, close cursor and connection to db to free ressources
cursor.close()
db.close()
