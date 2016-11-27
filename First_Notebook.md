

```python
import pandas as pd
```


```python
data = pd.read_csv('enrollments.csv')
```


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>account_key</th>
      <th>status</th>
      <th>join_date</th>
      <th>cancel_date</th>
      <th>days_to_cancel</th>
      <th>is_udacity</th>
      <th>is_canceled</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>448</td>
      <td>canceled</td>
      <td>2014-11-10</td>
      <td>2015-01-14</td>
      <td>65</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>448</td>
      <td>canceled</td>
      <td>2014-11-05</td>
      <td>2014-11-10</td>
      <td>5</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>448</td>
      <td>canceled</td>
      <td>2015-01-27</td>
      <td>2015-01-27</td>
      <td>0</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>448</td>
      <td>canceled</td>
      <td>2014-11-10</td>
      <td>2014-11-10</td>
      <td>0</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>448</td>
      <td>current</td>
      <td>2015-03-10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
#breast = read_txt('BREAST.TXT')
path = 'BREAST.TXT'
#using pandas with a column specification

```

# col_specification = [(0, 9), (9, 15)(16, 21)]


```python

col_specification = [(0,14), (15,22), (23,33),(34,42), (42,45)]
data = pd.read_fwf(path, colspecs = col_specification)
```


```python
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>07000003000000</th>
      <th>502201</th>
      <th>20601932</th>
      <th>02111992</th>
      <th>C50</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7000057000000</td>
      <td>502501</td>
      <td>20761920</td>
      <td>2061996</td>
      <td>C50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7000066000000</td>
      <td>502501</td>
      <td>20701924</td>
      <td>2061994</td>
      <td>C50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7000078000000</td>
      <td>502201</td>
      <td>20591917</td>
      <td>2031977</td>
      <td>C50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7000091000000</td>
      <td>502501</td>
      <td>20651946</td>
      <td>2102011</td>
      <td>C50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7000109000000</td>
      <td>502502</td>
      <td>20611924</td>
      <td>2051986</td>
      <td>C50</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
