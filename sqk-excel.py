import mysql.connector
import openpyxl

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='Password@12',
                              host='localhost', database='my_database')

# Open the Excel file containing the SQL queries
wb = openpyxl.load_workbook('queries.xlsx')

# Select the sheet containing the queries
sheet = wb['Sheet1']

# Loop through the rows in the sheet and execute each query
for row in sheet.iter_rows(min_row=2, values_only=True):
    query = row[0]
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()
    cursor.close()

# Close the database connection
cnx.close()
