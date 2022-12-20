import pandas as pd

# Read csv files
df_processed_data = pd.read_csv('./data/processed_data.csv', index_col=[0])
df_new_data = pd.read_csv('./data/new_data.csv', index_col=[0])

# Joining
df_ = pd.concat([df_processed_data, df_new_data], axis=1)

# Saving to csv file
df_.to_csv('./data/samambaia_houses.csv')