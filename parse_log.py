import re
# FYI, "re" library is reg ex
import pandas as pd

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

# There are 13 columns to output originally
# Open to add the other columns
dimensions = ['Scenario', 'Year', 'Period', 'View', 'Entity',
              'Value', 'Account', 'ICP', 'Custom1', 'Custom2',
              'Custom3', 'Custom4','Amount']#,'Error Value','Error Message']
sample_df = pd.DataFrame(my_data, columns = dimensions)

# Only keep lines with 'ERROR' in the DataFrame
error_only_df = sample_df[sample_df['Scenario'].str.contains('ERROR')]
error_only_df.reset_index(drop = True, inplace = True)
middle_df = error_only_df.drop(error_only_df.head(1).index)\
                         .drop(error_only_df.tail(1).index)

middle_df['Scenario'] = middle_df['Scenario'].str[37:]



#middle_df.to_excel("output14.xlsx")

'''
with open(selected_file) as f:
    f = f.readlines()

for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break
'''

# This just helps check to see if the log file I'm reading
    # is still reading.
#print(working_file.read())

#working_file.close()