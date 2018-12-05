import pandas as pd
from pymongo import MongoClient
from config import (mongo_name, mongo_pass)

client = MongoClient(f'mongodb://{mongo_name}:{mongo_pass}@ds249818.mlab.com:49818/heroku_6lctns1z')
db = client.heroku_6lctns1z
collection = db.sales_data

sales_csv = pd.read_csv('Sample_Data_Set_for_UCI_Project_2.csv')


new_keys_list = []
for x in range(0, 9090):
    key = f'_{x}'
    new_keys_list.append(key)

new_keys_df = pd.Series(new_keys_list)

sales_csv['new_key'] = pd.Series(new_keys_list, index=sales_csv.index)
sales_csv = sales_csv.set_index('new_key')


sales_list = []
sales_dict = sales_csv.to_dict('index')
sales_list.append(sales_dict)
sales_list = list(sales_list[0].values())


for x in sales_list:
    collection.insert_one(x)

