# Learning Objectives

**What's a database?**
   - A database is a structured collection of data. It's like an organized filing system where you can store and retrieve information.

**What's a relational database?**
   - A relational database is a type of database that organizes data into tables with rows and columns. The tables can be related to each other through keys.

**What does SQL stand for?**
   - SQL stands for Structured Query Language. It's a language used to manage and manipulate relational databases.

**What's MySQL?**
   - MySQL is a popular open-source relational database management system. It's software that allows you to create and manage relational databases.

**How to create a database in MySQL?**
   - Example:
     ```sql
     CREATE DATABASE your_database_name;
     ```

**What does DDL and DML stand for?**
   - DDL stands for Data Definition Language (dealing with the structure of the database), and DML stands for Data Manipulation Language (dealing with the data within the database).

**How to CREATE or ALTER a table?**
   - Example of creating a table:
     ```sql
     CREATE TABLE your_table_name (
       column1 datatype,
       column2 datatype,
       ...
     );
     ```
   - Example of altering a table (adding a new column):
     ```sql
     ALTER TABLE your_table_name
     ADD COLUMN new_column datatype;
     ```

**How to SELECT data from a table?**
   - Example:
     ```sql
     SELECT column1, column2
     FROM your_table_name
     WHERE condition;
     ```

**How to INSERT, UPDATE, or DELETE data?**
   - Example of inserting data:
     ```sql
     INSERT INTO your_table_name (column1, column2)
     VALUES (value1, value2);
     ```
   - Example of updating data:
     ```sql
     UPDATE your_table_name
     SET column1 = new_value
     WHERE condition;
     ```
   - Example of deleting data:
     ```sql
     DELETE FROM your_table_name
     WHERE condition;
     ```

**What are subqueries?**
    - Subqueries are queries embedded within other queries. They are used to retrieve data that will be used in the main query.

**How to use MySQL functions?**
    - Example of using a MySQL function (finding the total number of rows in a table):
      ```sql
      SELECT COUNT(*)
      FROM your_table_name;
      ```
  