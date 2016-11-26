

```python
import unicodecsv

enrollments_filename = 'enrollments.csv'
```


```python
with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
    
```


```python
enrollments[0]
```




    {u'account_key': u'448',
     u'cancel_date': u'2015-01-14',
     u'days_to_cancel': u'65',
     u'is_canceled': u'True',
     u'is_udacity': u'True',
     u'join_date': u'2014-11-10',
     u'status': u'canceled'}




```python
engagements_filename = 'daily_engagement.csv'
```


```python
with open(engagements_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)
```


```python
daily_engagement[0]
```




    {u'acct': u'0',
     u'lessons_completed': u'0.0',
     u'num_courses_visited': u'1.0',
     u'projects_completed': u'0.0',
     u'total_minutes_visited': u'11.6793745',
     u'utc_date': u'2015-01-09'}




```python
submissions_filename = 'project_submissions.csv'
```


```python
with open(submissions_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)
```


```python
project_submissions[0]
```




    {u'account_key': u'256',
     u'assigned_rating': u'UNGRADED',
     u'completion_date': u'2015-01-16',
     u'creation_date': u'2015-01-14',
     u'lesson_key': u'3176718735',
     u'processing_state': u'EVALUATED'}




```python

```
