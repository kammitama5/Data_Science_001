
# coding: utf-8

# In[1]:

import pandas as pd


# In[3]:

x = (1, 'a', 2, 'b')
type(x)


# In[4]:

x = [1, 'a', 2, 'b']
type(x)


# In[6]:

x.append(3.3)
print(x)


# In[7]:

for item in x:
    print(item)


# In[8]:

i = 0
while(i != len(x)):
    print(x[i])
    i = i + 1
    


# In[9]:

1 in [1, 2, 3]


# In[10]:

x = 'This is a string'
print(x[0])
print(x[0:1])
print(x[0:2])


# In[11]:

x[-1]


# In[12]:

x[-4:-2]


# In[13]:

x[:3]


# In[15]:

x[3:]


# In[18]:

x = 'Dr. Christopher Brooks'
print(x[3:15])


# In[19]:

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0]
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1]
print(firstname)
print(lastname)


# In[20]:

x= {'Christopher Brooks':'brooksch@umich.edu', 'Bill Gates' : 'billg@microsoft.com'}
x['Christopher Brooks']


# In[21]:

x['Kevyn Collins-Thompson'] = None
x['Kevyn Collins-Thompson']


# In[22]:

for name in x:
    print(x[name])


# In[23]:

for name, email in x.items():
    print(name)
    print(email)


# x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
# fname, lname, email = x

# In[28]:

fname


# In[29]:

lname


# In[30]:

email


# In[31]:

x = ('Christopher', 'Brooks', 'brooksch@umich.edu', 'Ann Arbor')


# In[32]:

print('Chris' + str(2))


# In[34]:

sales_record = {'price' : 3.24,
               'num_items' : 4,
               'person' : 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                            sales_record['num_items'],
                            sales_record['price'],
                            sales_record['num_items'] * sales_record['price']))


# In[40]:

import csv
get_ipython().magic('precision 2')

with open('mpg.csv') as csvfile:
          mpg = list(csv.DictReader(csvfile))
          mpg[:3]
         


# In[41]:

mpg[:3]


# In[42]:

len(mpg)


# In[43]:

mpg[0].keys()


# In[45]:

sum(float(d['cty']) for d in mpg) / len(mpg)


# In[46]:

sum(float(d['hwy']) for d in mpg)/ len(mpg)


# In[48]:

cylinders = set(d['cyl'] for d in mpg)
cylinders


# In[49]:

CtyMpgByCyl = []
for c in cylinders:
    summpg = 0
    cyltypecount = 0
    for d in mpg:
        if d['cyl'] == c:
            summpg += float(d['cty'])
            cyltypecount += 1
    CtyMpgByCyl.append((c, summpg / cyltypecount))
    
CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl


# In[50]:

vehicleclass = set(d['class'] for d in mpg)
vehicleclass


# In[52]:

HwyMpgByClass = []

for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg:
        if d['class'] == t:
            summpg += float(d['hwy'])
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount))
    

HwyMpgByClass.sort(key=lambda x: x[1])
HwyMpgByClass
            
    


# In[ ]:



