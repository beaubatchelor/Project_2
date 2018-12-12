
# coding: utf-8

# In[1]:


import pandas as pd
from pymongo import MongoClient
from pprint import pprint
from data.config import (mongo_name, mongo_pass)


# In[2]:


client = MongoClient(f'mongodb://{mongo_name}:{mongo_pass}@ds249818.mlab.com:49818/heroku_6lctns1z')
db = client.heroku_6lctns1z
collection = db.sales_data
master_list = list(collection.find({}, {'_id': False}))


# In[4]:


master_df = pd.DataFrame(master_list)


# In[14]:


groupby_df = master_df.groupby(['Lines','Year','Month']).agg({'Sales revenue' : 'sum'})


# In[16]:


groupby_df = groupby_df.reset_index()


# In[94]:


# groupby_df.head(100)
# groupby_df.dtypes
# test_df = groupby_df.loc[groupby_df["Sales revenue"] == 6186.200000000002]
# test_df.head(100)


# In[150]:


years = {
    2014 : {"x" : [1,2,3,4,5,6,7,8,9,10,11,12],"y" : [], "mode" : "lines", "name" : "2014"},
    2015 : {"x" : [1,2,3,4,5,6,7,8,9,10,11,12],"y" : [], "mode" : "lines", "name" : "2015"},
    2016 : {"x" : [1,2,3,4,5,6,7,8,9,10,11,12],"y" : [], "mode" : "lines", "name" : "2016"},
}
lines = []
db_entry = []

for i in range(0,len(master_list)):
    new_line = master_list[i]['Lines']
    new_line = new_line.replace(" ", "_")
    if new_line not in lines:
        lines.append(new_line)


# In[151]:


for line in lines:
    entry = {line : years}
    db_entry.append(entry)


# In[152]:


# pprint(db_entry[1])


# In[153]:


for entry in db_entry:
    prod_list = list(entry.keys())
    prod_line = prod_list[0]
    for year in entry[prod_line]:
        sales_sum_list = entry[prod_line][year]["y"]
        counter = 1
        for index, row in groupby_df.iterrows():
            df_line = row[0].replace(" ", "_")
            if df_line == prod_line and row[1] == year and row[2] == counter:
                print(prod_line)
                print(year)
                print(counter)
                counter += 1
#             df_line = row[0].replace(" ", "_")
#             if df_line == prod_line and row[1] == year and row[2] == counter:
#                 sales_sum_list.append(round(row[3], 2))
#                 counter += 1
# pprint(db_entry)

    


# In[144]:


# db_entry[1]['City_Skirts'][2014]['y']


# In[145]:


# db_entry[0]['Accessories'][2014]['y']


# In[154]:


get_ipython().system('jupyter nbconvert --to script by_month_cleaner.ipynb')

