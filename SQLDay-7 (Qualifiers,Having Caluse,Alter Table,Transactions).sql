mysql> use sql_lab;
Database changed
mysql> -- Task 1: Create Person table with columns PersonID, FirstName, LastName, and Age.
mysql> -- Make PersonID the primary key.
mysql>
mysql> CREATE TABLE Person (
    ->     PersonID int PRIMARY KEY,
    ->     FirstName varchar(255),
    ->     LastName varchar(255),
    ->     Age int
    -> );
Query OK, 0 rows affected (0.07 sec)

mysql> desc Person;
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| PersonID  | int          | NO   | PRI | NULL    |       |
| FirstName | varchar(255) | YES  |     | NULL    |       |
| LastName  | varchar(255) | YES  |     | NULL    |       |
| Age       | int          | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
4 rows in set (0.08 sec)

mysql> -- Task 2: Create Employee table with columns emp_id, first_name, last_name, and age.
mysql> -- Make emp_id the primary key.
mysql>
mysql> CREATE TABLE Employee (
    ->     emp_id int PRIMARY KEY,
    ->     first_name varchar(255),
    ->     last_name varchar(255),
    ->     age int
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> desc Employee;
+------------+--------------+------+-----+---------+-------+
| Field      | Type         | Null | Key | Default | Extra |
+------------+--------------+------+-----+---------+-------+
| emp_id     | int          | NO   | PRI | NULL    |       |
| first_name | varchar(255) | YES  |     | NULL    |       |
| last_name  | varchar(255) | YES  |     | NULL    |       |
| age        | int          | YES  |     | NULL    |       |
+------------+--------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

mysql> -- Task 3: Insert data into Person table.
mysql> INSERT INTO Person (PersonID, FirstName, LastName, Age) VALUES
    -> (1, 'Ismail', 'Khan', 23),
    -> (2, 'Rushikesh', 'Shardul', 22),
    -> (3, 'Aanchal', 'Saini', 24),
    -> (4, 'Sonali', 'Thule', 24),
    -> (5, 'Kunal', 'Dhamal', 20);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select*from Person;
+----------+-----------+----------+------+
| PersonID | FirstName | LastName | Age  |
+----------+-----------+----------+------+
|        1 | Ismail    | Khan     |   23 |
|        2 | Rushikesh | Shardul  |   22 |
|        3 | Aanchal   | Saini    |   24 |
|        4 | Sonali    | Thule    |   24 |
|        5 | Kunal     | Dhamal   |   20 |
+----------+-----------+----------+------+
5 rows in set (0.00 sec)

mysql> -- Task 4: Insert data into Employee table.
mysql> INSERT INTO Employee (emp_id, first_name, last_name, age) VALUES
    -> (101, 'Faisal', 'Shaikh', 25),
    -> (102, 'Fazal', 'Munshi', 19),
    -> (103, 'Akansha', 'Kotian', 24),
    -> (104, 'Anit', 'Gupta', 21),
    -> (105, 'Fairaaz', 'Ahmed', 19);
Query OK, 5 rows affected (0.05 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select*from Employee;
+--------+------------+-----------+------+
| emp_id | first_name | last_name | age  |
+--------+------------+-----------+------+
|    101 | Faisal     | Shaikh    |   25 |
|    102 | Fazal      | Munshi    |   19 |
|    103 | Akansha    | Kotian    |   24 |
|    104 | Anit       | Gupta     |   21 |
|    105 | Fairaaz    | Ahmed     |   19 |
+--------+------------+-----------+------+
5 rows in set (0.00 sec)

mysql> -- Task 5: Create Union of two tables to get combined results from Person and Employee tables.
mysql>
mysql> SELECT PersonID AS ID, FirstName, LastName, Age FROM Person
    -> UNION
    -> SELECT emp_id AS ID, first_name AS FirstName, last_name AS LastName, age AS Age FROM Employee;
+-----+-----------+----------+------+
| ID  | FirstName | LastName | Age  |
+-----+-----------+----------+------+
|   1 | Ismail    | Khan     |   23 |
|   2 | Rushikesh | Shardul  |   22 |
|   3 | Aanchal   | Saini    |   24 |
|   4 | Sonali    | Thule    |   24 |
|   5 | Kunal     | Dhamal   |   20 |
| 101 | Faisal    | Shaikh   |   25 |
| 102 | Fazal     | Munshi   |   19 |
| 103 | Akansha   | Kotian   |   24 |
| 104 | Anit      | Gupta    |   21 |
| 105 | Fairaaz   | Ahmed    |   19 |
+-----+-----------+----------+------+
10 rows in set (0.00 sec)

mysql>