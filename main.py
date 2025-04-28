import pandas as pd


wine_data=pd.read_csv('WineQT.csv')

first_five_row=wine_data.head()
print(first_five_row)