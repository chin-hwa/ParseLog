import re
import pandas as pd

selected_file = "dummy.log"

# Open() method with the "r", "a", "w', and "x" arguemnts will
    # make it read-only, append, write, and create respectively

working_file = open(selected_file, "r")

'''
with open(selected_file) as f:
    f = f.readlines()

for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break
'''

print(working_file.read())

working_file.close()