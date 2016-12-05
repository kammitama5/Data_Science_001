
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt


# In[15]:

year = [1950, 1951, 1952,]
pop = [2.538, 2.57, 2.62]


# In[16]:

plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10],
          ['0', '2B', '4B', '6B', '8B', '10B']) # must be same length as first list 

# Add more data
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop
plt.show()


# In[ ]:



