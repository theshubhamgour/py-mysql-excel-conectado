# py-mysql-excel-conectado
Python script reads SQL queries from an Excel sheet, executes them on a MySQL database, and updates the data.

# Description
This Python project takes an Excel sheet containing SQL queries as input and executes them using the MySQL Connector library to fetch data from a MySQL database. The project connects to a database with two tables, "table1" and "table2", and then inserts five rows of data into them. The "table2" table is connected to "table1" with a foreign key constraint.

The project uses the openpyxl library to read the Excel sheet and extract the SQL queries. It then uses the mysql.connector library to connect to the MySQL database, execute the queries, and fetch the data. After executing each query, it commits the changes to the database and then closes the cursor. Finally, it closes the database connection.

This project is particularly useful for automating repetitive database tasks, such as inserting data into tables from an Excel sheet, without the need for manual input.

# After Release v2

We Created a Database named ```my_database``` in which we created tables for demonstrating the project

![image](https://user-images.githubusercontent.com/72512204/233977792-bb62a93f-9af8-4d5e-bb7a-57c94073041a.png)

There are three tables namely - ```table1``` ```table2``` and ```users```

![image](https://user-images.githubusercontent.com/72512204/233978186-eb6d3574-5939-4c35-90c7-79fd19d55eef.png)

Below we have created the sample tables for demostration purpose

![image](https://user-images.githubusercontent.com/72512204/233978602-412cc531-ccd8-4009-8a64-7d3d3dc1a14d.png)

This is the sheet where the SQL queries are entered as input.

![image](https://user-images.githubusercontent.com/72512204/233976983-b44c425d-3c37-4ce7-b806-350c3f6c6412.png)


This is the output after running the program

![image](https://user-images.githubusercontent.com/72512204/233977298-2424a8fe-3142-4eee-9487-dac96e91f0b5.png)


