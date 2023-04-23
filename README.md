# py-mysql-excel-conectado
Python script reads SQL queries from an Excel sheet, executes them on a MySQL database, and updates the data.

# Description
This Python project takes an Excel sheet containing SQL queries as input and executes them using the MySQL Connector library to fetch data from a MySQL database. The project connects to a database with two tables, "table1" and "table2", and then inserts five rows of data into them. The "table2" table is connected to "table1" with a foreign key constraint.

The project uses the openpyxl library to read the Excel sheet and extract the SQL queries. It then uses the mysql.connector library to connect to the MySQL database, execute the queries, and fetch the data. After executing each query, it commits the changes to the database and then closes the cursor. Finally, it closes the database connection.

This project is particularly useful for automating repetitive database tasks, such as inserting data into tables from an Excel sheet, without the need for manual input. 
