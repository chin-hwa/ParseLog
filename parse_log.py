import re
# FYI, "re" library is reg ex
import pandas as pd

selected_file = "dummy.log"

# Open() method with the "r", "a", "w', and "x" arguemnts will
    # make it read-only, append, write, and create respectively

# Be sure to uncomment the .close() below if using this one
#working_file = open(selected_file, "r")


#  *** KEEP the Code Snippet for reference!!!***

with open(selected_file) as f:
    my_data = []
    lines = f.readlines()
    for line in lines:
        my_data.append(re.split(";",line.strip()))

sample_df = pd.DataFrame(my_data)

sample_df.to_excel("output.xlsx")

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