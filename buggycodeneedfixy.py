
# coding: utf-8

# In[19]:

import pandas as pd
import numpy as np
# Set ipython's max row display
pd.set_option('display.max_row', 1000)
# Set iPython's max column width to 50
pd.set_option('display.max_columns', 50)


# In[20]:

import unicodecsv


# In[21]:

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
    
enrollments = pd.read_csv('enrollments.csv')
daily_engagement = pd.read_csv('daily_engagement.csv')
project_submissions = pd.read_csv('project_submissions.csv')


# In[ ]:




# In[22]:

enrollments.head()



# In[23]:

daily_engagement.head()


# In[24]:

project_submissions.head()


# In[26]:

type(enrollments)


# In[35]:

len(daily_engagement)
    


# In[39]:

len(project_submissions)


# In[42]:

'''
unique_enrolled_students = set()
for enrollment in enrollments:
    unique_enrolled_students.add(enrollment['account_key])
len(unique_enrolled_students)

'''


# In[43]:

'''
unique_engagement_students = set()
for engagement_record in daily_engagement:
    unique_engagement_students.add(engagement_record['acct])
len(unique_engagement_students)
'''


# In[44]:

'''
unique_project_submitters = set()
for submission in project_submissions:
    unique_project_submitters.add(submission['account_key])
len(unique_project_submitters)
'''


# In[ ]:



