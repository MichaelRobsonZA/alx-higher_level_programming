#!/bin/bash

# Get the list of SQL files in the current directory
sql_files=$(ls *.sql)

# MySQL connection parameters
mysql_user="root"
mysql_password="root"

# Loop through each SQL file and execute it
for file in $sql_files; do
  echo "Executing $file..."
  mysql -u $mysql_user -p$mysql_password < $file
done
