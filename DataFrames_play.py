
# coding: utf-8

# In[2]:

import pandas as pd


# In[4]:

animals = ['tiger', 'bear', 'moose']
pd.Series(animals)


# In[5]:

numbers = [1, 2, 3]
pd.Series(numbers)


# In[6]:

animals = ['Tiger', 'Bear', None]
pd.Series(animals)


# In[7]:

numbers = [1, 2, None]
pd.Series(numbers)


# In[8]:

import numpy as np
np.nan == None


# In[9]:

np.isnan(np.nan)


# In[19]:

sports = {'Archery' : 'Bhutan',
         'Golf' : 'Scotland',
         'Sumo' : 'Japan',
         'Taekwondo' : 'South Korea'}
s = pd.Series(sports)
s


# In[21]:

s.iloc[3]


# In[22]:

s.loc['Golf']


# In[23]:

s[3]


# In[24]:

s['Golf']


# In[30]:

s = pd.Series([100.00, 120.00, 101.00, 3.00])
s


total = 0
for item in s:
    total += item
print(total)


# In[31]:

import numpy as np
total = np.sum(s)
print(total)


# In[32]:

s = pd.Series(np.random.randint(0, 1000, 10000))
s.head()


# In[33]:

len(s)


# In[35]:

get_ipython().run_cell_magic('timeit', '-n 100', 'summary = 0\nfor item in s:\n    summary += item')


# In[36]:

get_ipython().run_cell_magic('timeit', '-n 100', 'summary = np.sum(s)')


# In[37]:

s += 2
s.head()


# In[38]:

for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()
    


# In[39]:

get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0, 1000, 10000))\nfor label, value in s.iteritems():\n    s.loc[label] = value+2\n    ')


# In[40]:

get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0, 1000, 10000))\ns += 2')


# In[42]:

s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s


# In[43]:

original_sports = pd.Series({'Archery' : 'Bhutan',
                            'Golf' : 'Scotland',
                            'Sumo' : 'Japan',
                            'Taekwondo' : 'South Korea'})


# In[44]:

cricket_loving_countries = pd.Series(['Australia',
                                     'Barbados',
                                     'Pakistan',
                                     'England'],
                                    index = ['Cricket',
                                            'Cricket',
                                            'Cricket',
                                            'Cricket'])

all_countries = original_sports.append(cricket_loving_countries)


# In[45]:

original_sports


# In[46]:

import pandas as pd


# In[48]:

purchase_1 = pd.Series({'Name': 'Chris',
                      'Item Purchased' : 'Dog Food',
                      'Cost' : 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                      'Item Purchased' : 'Kitty Litter',
                      'Cost' : 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                      'Item Purchased' : 'Bird Seed',
                      'Cost' : 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index = ['Store 1', 'Store 1', 'Store 2'])


# In[49]:

df.head()


# In[52]:

df.iloc[2]


# In[53]:

df.iloc[0:2]


# In[57]:

df.loc['Store 1']


# In[58]:

df.loc['Store 2']


# In[60]:

type(df.loc['Store 2']) # my result


# In[81]:

df.iloc[0:, 1]


# In[82]:

df['Item Purchased'] # result given


# In[83]:

df.loc['Store 1', 'Cost']


# In[84]:

df.T


# In[ ]:




# In[86]:

df.loc['Store 1']['Cost']


# In[87]:

# get name and cost
df


# In[93]:

df.iloc[:3] 


# In[98]:

df.loc[:, ['Name', 'Cost']]


# In[127]:

# my solution

df.iloc[:,0] * .80



# In[128]:

# their solution
df['Cost'] *= 0.8
print(df)


# In[ ]:



