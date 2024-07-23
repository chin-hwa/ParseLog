import re
# FYI, "re" library is reg ex
import pandas as pd
import numpy as np

selected_file = "dummy.log"

# Open() method with the "r", "a", "w', and "x" arguemnts will
    # make it read-only, append, write, and create respectively

# Be sure to uncomment the .close() below if using this one
#working_file = open(selected_file, "r")


#  *** KEEP the Code Snippet for reference!!!***

# The readlines() method reads all lines from a file
    # This method is good if file size is small
    # and performance is not important

with open(selected_file) as f:
    my_data = []
    lines = f.readlines()
    for line in lines:
        my_data.append(re.split(";",line.strip()))

# There are 13 columns to output originally.  Need 3 more columns
dimensions = ['Scenario', 'Year', 'Period', 'View', 'Entity',
              'Value', 'Account', 'ICP', 'Custom1', 'Custom2',
              'Custom3', 'Custom4','Amount']
sample_df = pd.DataFrame(my_data, columns = dimensions)

# Only keep lines with 'ERROR' in the DataFrame
error_only_df = sample_df[sample_df['Scenario'].str.contains('ERROR')]
#error_only_df.reset_index(drop = True, inplace = True)

# Remove the 1st and last line of "ERROR" lines
middle_df = error_only_df.drop(error_only_df.head(1).index)\
                         .drop(error_only_df.tail(1).index)

# Cut off the leftmost 37 characters of the 'Scenario' column
middle_df['Scenario'] = middle_df['Scenario'].str[37:]

# Create a new column called 'Error Values' from
    # the 3rd row in the 'Scenario' column
raw_EV = []
for values in middle_df['Scenario']:
    if ">>>>>>" in values:
        raw_EV.append(values)
    else:
        raw_EV.append('')

raw_EV = [elem.replace('>>>>>>', '') for elem in raw_EV]
print(raw_EV)

#middle_df.to_excel("output3.xlsx")

#working_file.close()