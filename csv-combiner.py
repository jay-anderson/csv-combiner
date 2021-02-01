#!/usr/bin/env python3
#shebang should work for everyone

"""purpose: write a command line program that takes several
csv files as arguments. Each CSV file will have the same columns.
Your script should output a new CSV file to stdout that contains
the rows from each of the inputs along with an additional column
that has the filename from which the row came (only the file's basename,
not the entire path). Use filename as the header for the additional
column.


 in short, csv manipulation

"""
##################################
#imports
import pandas as pd
import os
import sys
##################################
#parse arguments for manipulation

# counts the number of args
count = len(sys.argv)

# empty list to store csv files
csv = []

# converts to dataframe and adds to a csv list
for i in range(1, count):
    #reads in each csv path
    df = pd.read_csv(sys.argv[i], index_col=0)
    #adds a new column for file name and populates w/ file basename
    df['filename'] = os.path.basename(sys.argv[i])
    #appends newly creates and altered df to csv list
    csv.append(df)

#new dataframe combined_df set equal to first datafrane in csv
combined_df = csv[0]

#append each dataframe in csv to combined_df to create one dataframe that includes all csv files and filename column
for i in range(1, len(csv)):
    combined_df = combined_df.append(csv[i])


# csv files are outputted as stdout
combined_df.to_csv(path_or_buf=sys.stdout)
#the command '> combined.csv' will create a new file of that name and populate with this df