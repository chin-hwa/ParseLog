import pandas as pd

dataset = {'Entity': [100000, 200000, '300000'],
           'ICP': [199999, 299999, '399999']}

account = ['0001', '0002', '0003', '2140']

# pd.melt() method unpivots the dataframe
#my_df = pd.melt(my_df, ignore_index = False).reset_index()

sample_set = pd.DataFrame(dataset)

print(sample_set)

