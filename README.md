# csv-combiner
Combines several csv files and appends a column with each individual file basename

Specified Directions: 
Write a command line program that takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns. Your script should output a new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came (only the file's basename, not the entire path). Use filename as the header for the additional column.


Run the code using the following command.
$ ./csv-combiner.php ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv

Code was tested using Ubuntu on a Windows OS. Features the following shebang line '#!/usr/bin/env python3'
This should work regardless of the location that python is installed, but it may need to be altered if you're using an
older version of python. 


No restrictions regarding the number of csv files. 
