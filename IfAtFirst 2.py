
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


# In[12]:

import unicodecsv

enrollments = []
with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
    
    for row in reader:
        enrollments.append(row)
        
print enrollments[0]


# In[13]:

enrollments_filename = 'enrollments.csv'
with open(enrollments_filename, 'rb') as f:
    reader3 = unicodecsv.DictReader(f)
    enrollments = list(reader3)
print enrollments[0]
    


# In[16]:

engagements_filename = 'daily_engagement.csv'

with open(engagements_filename, 'rb') as f:
    reader2 = unicodecsv.DictReader(f)
    daily_engagement = list(reader2)

print daily_engagement[0]


# In[15]:

submissions_filename = 'project_submissions.csv'

with open(submissions_filename, 'rb') as f:
    reader1 = unicodecsv.DictReader(f)
    project_submissions = list(reader1)
    
print project_submissions[0]


# In[ ]:



