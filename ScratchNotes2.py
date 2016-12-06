
# coding: utf-8

# In[1]:

import datetime as dt
import time as tm



# In[2]:

tm.time()


# In[3]:

dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow


# In[4]:

dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second


# In[5]:

delta = dt.timedelta(days = 100)
delta


# In[6]:

today = dt.date.today()


# In[7]:

today-delta


# In[8]:

today > today-delta


# In[10]:

class Person:
    department = 'School of Information'
    
    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location


# In[22]:

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
cheapest


# In[30]:

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))


# In[31]:

my_function = lambda a, b, c : a + b


# In[32]:

my_function(1, 2, 3)


# In[33]:

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


# In[34]:

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]


# In[42]:

for person in people:
    print(split_title_and_name(person) == (lambda person: person[-1]))


# In[ ]:

list(map(split_title_and_name, people)) == list(map())

