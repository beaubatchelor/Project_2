import pandas as pd
from pymongo import MongoClient
from pprint import pprint
from config import (mongo_name, mongo_pass)

client = MongoClient(f'mongodb://{mongo_name}:{mongo_pass}@ds249818.mlab.com:49818/heroku_6lctns1z')
db = client.heroku_6lctns1z
collection = db.sales_data

master_list = list(collection.find({}, {'_id': False}))

cities = []
lines = []
city_list = []

for i in range(0,len(master_list)):
    if master_list[i]['City'] not in cities:
        cities.append(master_list[i]['City'])
for i in range(0,len(master_list)):
    if master_list[i]['Lines'] not in lines:
        lines.append(master_list[i]['Lines'])

for i in range(0,len(cities)):
    city_list = city_list + [{'City': cities[i], 'Lines with Quantity': [], 'Lines with Sales': [], 'Lines with Margin': []}]


for j in range (0, len(city_list)):
    qty_lines_dict = {}
    for i in range(0, len(lines)):
        qty_lines_dict[lines[i]] = 0
    city_list[j]['Lines with Quantity'].append(qty_lines_dict)
    
for j in range (0, len(city_list)):
    sales_lines_dict = {}
    for i in range(0, len(lines)):
        sales_lines_dict[lines[i]] = 0
    city_list[j]['Lines with Sales'].append(sales_lines_dict)
    
for j in range (0, len(city_list)):
    margin_lines_dict = {}
    for i in range(0, len(lines)):
        margin_lines_dict[lines[i]] = 0            
    city_list[j]['Lines with Margin'].append(margin_lines_dict)
    
for i in range(0,len(cities)):
    for j in range(0, len(lines)):
        city_line_quantity = 0
        city_line_sales = 0
        city_line_margin = 0
        for k in range(0, len(master_list)):
            if master_list[k]['City'] == cities[i] and master_list[k]['Lines'] == lines[j]:
                city_line_quantity += master_list[k]['Quantity sold']
                city_line_sales += master_list[k]['Sales revenue']
                city_line_margin += master_list[k]['Margin']
        city_list[i]['Lines with Quantity'][0][lines[j]] = round(city_line_quantity,3)
        city_list[i]['Lines with Sales'][0][lines[j]] = round(city_line_sales,3)
        city_list[i]['Lines with Margin'][0][lines[j]] = round(city_line_margin,3)
city_list