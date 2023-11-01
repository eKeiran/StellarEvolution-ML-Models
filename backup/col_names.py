import pandas as pd

file_path = './clusters.csv'

column_names = ['Cl', 'E(B-V) mag', 'True Distance(m-M mag)','Model','ClName']

df = pd.read_csv(file_path, header=None, encoding='ISO-8859-1')

df.columns = column_names

df.to_csv(file_path, index=False, encoding='utf-8')
