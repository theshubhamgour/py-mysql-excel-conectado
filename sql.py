import mysql.connector

# Establish a connection to the database
cnx = mysql.connector.connect(user='root', password='Password@12',
                              host='localhost', database='amazon')

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Execute a SELECT query on the customers table
query = "SELECT * FROM customers"
cursor.execute(query)

# Fetch all rows of the result set
result = cursor.fetchall()

# Print each row
for row in result:
    print(row)

# Close the cursor and database connection
cursor.close()
cnx.close()
