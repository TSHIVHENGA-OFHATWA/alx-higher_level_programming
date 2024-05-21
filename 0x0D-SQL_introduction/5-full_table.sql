-- This script that prints the full description of the table first_table,
-- from the database hbtn_0c_0 in your MySQL server.
--SHOW TABLES;

-- This script prints the full description of the table `first_table`
-- from the database `hbtn_0c_0` in your MySQL server.

-- First, show the available tables in the database
SHOW TABLES FROM hbtn_0c_0;

-- Then, display the structure of the `first_table`
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0'
AND table_name = 'first_table';

