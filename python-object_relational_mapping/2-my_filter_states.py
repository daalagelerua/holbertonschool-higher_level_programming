#!usr/bin/pyhton3
"""
This script lists all states corresponding to
the given argument
"""

import MySQLdb  # To communicate with MySQL
import sys  # To retrieve the arguments passed to the script


if __name__ == "__main__":
    """No execution when imported"""

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",  # MySQL server adress (local here)
        port=3306,  # MySQL default port
        # Parameters
        user=sys.argv[1],   # User name
        passwd=sys.argv[2],  # Password
        db =sys.argv[3]       # Database name
    )

# Create a cursor object to execute sql requests and retrieve the results
cursor = db.cursor()

# Execute the query to get the state given as argument
state_name = sys.argv[4]  # Name of state will be the fourth argument
query = (
    "SELECT * FROM states WHERE name LIKE BINARY = '{}'"
    "ORDER BY id ASC".format(state_name)
)
cursor.execute(query)

# Fetch the results, prints a list of tuples (if states is found print it)
states = cursor.fetchall()
if states:
    for state in states:
        print(state)

# Once done, close cursor and connection to db to free ressources
cursor.close()
db.close()
