import pandas as pd
# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
pstat = pd.read_csv('3_sez_b.csv')

#r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
#ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols)

pstat