import pandas as pd
import os

dataset = {'Entity': [100000, 200000, '300000'],
           'ICP': [199999, 299999, '399999'],
           '0001': [234.40, 0, 2134.00],
           '0002': [2144.22, 422.00, 0],
           '2140': [993.00, 200, 24.00]}

sample_set = pd.DataFrame(dataset)

# pd.melt() method unpivots the dataframe
new_set = pd.melt(sample_set, id_vars = ['Entity', 'ICP'],
        var_name = 'Account', value_name= 'Amount')

#new_set.to_excel("output.xlsx")