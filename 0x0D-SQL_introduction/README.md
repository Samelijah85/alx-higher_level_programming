# SQL - Introduction
Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology you’re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology you’re using is stateless or stateful, you will need to persist your data somewhere. That’s what databases are for.

## Table of contents
* [Mandatory tasks](#mandatory-tasks)
  * [0. List databases](#0-list-databases)
  * [1. Create a database](#1-create-a-database)
  * [2. Delete a database](#2-delete-a-database)
  * [3. List tables](#3-list-tables)
  * [4. First table](#4-first-table)
  * [5. Full description](#5-full-description)
  * [6. List all in table](#6-list-all-in-table)
  * [7. First add](#7-first-add)
  * [8. Count 89](#8-count-89)
  * [9. Full creation](#9-full-creation)
  * [10. List by best](#10-list-by-best)
  * [11. Select the best](#11-select-the-best)
  * [12. Cheating is bad](#12-cheating-is-bad)
  * [13. Score too low](#13-score-too-low)
  * [14. Average](#14-average)
  * [15. Number by score](#15-number-by-score)
  * [16. Say my name](#16-say-my-name)
* [Advanced tasks](#advanced-tasks)
  * [17. Go to UTF8](#17-go-to-utf8)
  * [18. Temperatures #0](#18-temperatures-0)
  * [19. Temperatures #1](#19-temperatures-1)
  * [20. Temperatures #2](#20-temperatures-2)

## Mandatory tasks
### 0. List databases
Write a script that lists all databases of your MySQL server
[0-list_databases.sql](0-list_databases.sql)

### 1. Create a database
Write a script that creates the database `hbtn_0c_0` in your MySQL server.
- If the database `hbtn_0c_0` already exists, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements
[1-create_database_if_missing.sql](1-create_database_if_missing.sql)

### 2. Delete a database
Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
- If the database `hbtn_0c_0` doesn’t exist, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements
[2-remove_database.sql](2-remove_database.sql)

### 3. List tables
Write a script that lists all the tables of a database in your MySQL server.
* The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)
[3-list_tables.sql](3-list_tables.sql)

### 4. First table
Write a script that creates a table called `first_table` in the current database in your MySQL server.
* `first_table` description:
  - `id` INT
  - `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `first_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements
[4-first_table.sql](4-first_table.sql)

### 5. Full description
Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
* The database name will be passed as an argument of the `mysql` command
* You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements
[5-full_table.sql](5-full_table.sql)

### 6. List all in table
Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
- All fields should be printed
- The database name will be passed as an argument of the `mysql` command
[6-list_values.sql](6-list_values.sql)

### 7. First add
Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
- New row:
  - `id` = `89`
  - `name` = `Best School`
- The database name will be passed as an argument of the `mysql` command
[7-insert_value.sql](7-insert_value.sql)

### 8. Count 89
Write a script that displays the number of records with `id` = `89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
* The database name will be passed as an argument of the `mysql` command
[8-count_89.sql](8-count_89.sql)

### 9. Full creation
Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
* `second_table` description:
  * `id` INT
  * `name` VARCHAR(256)
  * `score` INT
* The database name will be passed as an argument to the `mysql` command
* If the table `second_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` and `SHOW` statements
* Your script should create these records:
  * `id` = 1, `name` = “John”, `score` = 10
  * `id` = 2, `name` = “Alex”, `score` = 3
  * `id` = 3, `name` = “Bob”, `score` = 14
  * `id` = 4, `name` = “George”, `score` = 8
[9-full_creation.sql](9-full_creation.sql)

### 10. List by best
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command
[10-top_score.sql](10-top_score.sql)

### 11. Select the best
Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command
[11-best_score.sql](11-best_score.sql)

### 12. Cheating is bad
Write a script that updates the score of Bob to `10` in the table `second_table`.
- You are not allowed to use Bob’s id value, only the `name` field
- The database name will be passed as an argument of the `mysql` command
[12-no_cheating.sql](12-no_cheating.sql)

### 13. Score too low
Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The database name will be passed as an argument of the `mysql` command
[13-change_class.sql](13-change_class.sql)

### 14. Average
Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The result column name should be `average`
- The database name will be passed as an argument of the `mysql` command
[14-average.sql](14-average.sql)

### 15. Number by score
Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- The result should display:
  - the `score`
  - the number of records for this `score` with the label `number`
- The list should be sorted by the number of records (descending)
- The database name will be passed as an argument to the `mysql` command
[15-groups.sql](15-groups.sql)

### 16. Say my name
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
- Don’t list rows without a `name` value
- Results should display the score and the name (in this order)
- Records should be listed by descending score
- The database name will be passed as an argument to the `mysql` command
[16-no_link.sql](16-no_link.sql)

## Advanced tasks
### 17. Go to UTF8
Write a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.

You need to convert all of the following to UTF8:
- Database `hbtn_0c_0`
- Table `first_table`
- Field name in `first_table`
[100-move_to_utf8.sql](100-move_to_utf8.sql)

### 18. Temperatures #0
Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)
- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
[101-avg_temperatures.sql](101-avg_temperatures.sql)

### 19. Temperatures #1
Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)
- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
[102-top_city.sql](102-top_city.sql)

### 20. Temperatures #2
Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)
- Write a script that displays the max temperature of each state (ordered by State name).
[103-max_state.sql](103-max_state.sql)
