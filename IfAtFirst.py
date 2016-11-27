
# coding: utf-8

# In[3]:

import unicodecsv

enrollments = []
f = open('enrollments.csv', 'rb')
reader = unicodecsv.DictReader(f)

for row in reader:
    enrollments.append(row)
    
f.close()

enrollments[0]


# In[2]:

# Data Acquisition
# Data Cleaning


# In[4]:

# if with statement used, do not need to close file. File 
# is closed automatically


# In[5]:

import unicodecsv

enrollments = []
with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    
    for row in reader:
        enrollments.append(row)
enrollments[0]


# In[6]:

import unicodecsv

enrollments = []
with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
    
    for row in reader:
        enrollments.append(row)
        
enrollments[0]


# In[10]:

enrollments_filename = 'enrollments.csv'
with open(enrollments_filename, 'rb') as f:
    reader3 = unicodecsv.DictReader(f)
    enrollments = list(reader3)
enrollments[0]
    


# In[11]:

engagements_filename = 'daily_engagement.csv'

with open(engagements_filename, 'rb') as f:
    reader2 = unicodecsv.DictReader(f)
    daily_engagement = list(reader2)

daily_engagement[0]


# In[9]:

submissions_filename = 'project_submissions.csv'

with open(submissions_filename, 'rb') as f:
    reader1 = unicodecsv.DictReader(f)
    project_submissions = list(reader1)
    
project_submissions[0]


# In[ ]:



