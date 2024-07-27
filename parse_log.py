import re
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog

def openFile():
    global selected_file 
    selected_file = filedialog.askopenfilename()

# Create the window for the app
root = Tk()
root.title("CC's Log Parser")
welcome_text = Label(root, text = "Please select a log file by pressing the button below!")
welcome_text.pack()

# Button for opening log file
open_button = Button(text = 'Select Log File', command = openFile)
open_button.pack()

# CLosing message
close_text = Label(root, text = "After selecting the log file, close the window to run the app.")
close_text.pack()
root.mainloop()

#selected_file = 'C:/Users/Chin-Hwa/Documents/Python Repo/dummy.log'

# The readlines() method reads all lines from a file
    # This method is good if file size is small
    # and performance is not important

# Take the log file and read every line, and use
    # the semicolon as the delimiter
with open(selected_file) as raw_file:
    my_data = []
    lines = raw_file.readlines()
    for line in lines:
        my_data.append(re.split(";",line.strip()))

print(my_data)
# Convert the list from the lines read into a DataFrame
# There are 13 columns to output originally.  Need 3 more columns
initial_dimensions = ['Scenario', 'Year', 'Period', 'View', 'Entity',
              'Value', 'Account', 'ICP', 'Custom1', 'Custom2',
              'Custom3', 'Custom4','Amount']
sample_df = pd.DataFrame(my_data, columns = initial_dimensions)

# Only keep lines with 'ERROR' in the DataFrame
error_only_df = sample_df[sample_df['Scenario'].str.contains('ERROR')]

# Remove the 1st and last line of "ERROR" lines
    # These only contain the initial timestamp
middle_df = error_only_df.drop(error_only_df.head(1).index)\
                         .drop(error_only_df.tail(1).index)

# Cut off the leftmost 37 characters of the 'Scenario' column
    # These are the timestamp prefix of the 1st column
middle_df['Scenario'] = middle_df['Scenario'].str[37:]

# Create a new column called 'Error Values' from
    # the 3rd row in the 'Scenario' column

# 1st, create a list for error values
raw_EV = []
for values in middle_df['Scenario']:
    if ">>>>>>" in values:
        raw_EV.append(values[6:])
    else:
        raw_EV.append(None)

# 2nd, convert the list into numpy array and
    # shift the values over by -1
EV_array = np.array(raw_EV)
adj_EV = np.roll(EV_array, -1)

# Last, insert the array as a new column
middle_df['Error Value'] = adj_EV.tolist()

# Create new columns called 'Line No' from
    # the 'Scenario' column

raw_line = []
for values in middle_df['Scenario']:

# Use regex to capture the text between:
    # 'Line: '
    # and
    # ', '
    result = re.search('Line: (.*),', values)
    if "Line: " in values:
        raw_line.append(int(result.group(1)))
    else:
        raw_line.append(None)

# Again, convert list into numpy array and shift
    # the values in the opposite direction this time
line_array = np.array(raw_line)
adj_line = np.roll(line_array, 1)

# Add to dataframe
middle_df['Line No'] = adj_line.tolist()

# Create new column called 'Error Messages' from the
    # 'Scenario' column.
    # The steps are very similar to the ones
    # above, but this time, a simple string
    # method called str.partition() will capture
    # all text after the delimiter

raw_EM = []
for values in middle_df['Scenario']:
    if "Line: " in values:
        raw_EM.append(values.partition(', Error: ')[2])
    else:
        raw_EM.append(None)

em_array = np.array(raw_EM)
adj_EM = np.roll(em_array, 1)

middle_df['Error Message'] = adj_EM.tolist()

# Drop all empty rows.  We need to use the column with 'Nan'
    # within the column values.  Pandas does not like
    # using empty strings.
no_null_df = middle_df.dropna(subset = ['Line No'])

# Rearrange the columns to our liking
dimensions = ['Line No',
              'Scenario',
              'Year', 
              'Period', 
              'View',
              'Entity',
              'Value',
              'Account',
              'ICP',
              'Custom1',
              'Custom2',
              'Custom3',
              'Custom4',
              'Amount',
              'Error Value',
              'Error Message']
final_df = no_null_df[dimensions]

# Reset the index numbers for all rows
final_df.reset_index(drop = True, inplace = True)

final_df.to_excel("output.xlsx")