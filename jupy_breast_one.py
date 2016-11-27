
# coding: utf-8

# In[8]:

import pandas as pd


# In[9]:

data = pd.read_csv('enrollments.csv')


# In[10]:

data.head()


# In[31]:

#breast = read_txt('BREAST.TXT')
path = 'BREAST.TXT'
#using pandas with a column specification


# # col_specification = [(0, 9), (9, 15)(16, 21)]

# In[72]:


col_specification = [(0,14), (15,22), (23,33),(34,42), (42,45),(46,49),(50,54),(55,59)]
data = pd.read_fwf(path, colspecs = col_specification)


# In[74]:

data.head()


# In[65]:

# name files in iteration
# use df['column_name]=data['text'].str(0:4)
# set each column
# print i to file


# In[ ]:



