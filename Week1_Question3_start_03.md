

```python
import pandas as pd
```


```python
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># Summer</th>
      <th>Gold</th>
      <th>Silver</th>
      <th>Bronze</th>
      <th>Total</th>
      <th># Winter</th>
      <th>Gold.1</th>
      <th>Silver.1</th>
      <th>Bronze.1</th>
      <th>Total.1</th>
      <th># Games</th>
      <th>Gold.2</th>
      <th>Silver.2</th>
      <th>Bronze.2</th>
      <th>Combined total</th>
      <th>ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>AFG</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>12</td>
      <td>5</td>
      <td>2</td>
      <td>8</td>
      <td>15</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>5</td>
      <td>2</td>
      <td>8</td>
      <td>15</td>
      <td>ALG</td>
    </tr>
    <tr>
      <th>Argentina</th>
      <td>23</td>
      <td>18</td>
      <td>24</td>
      <td>28</td>
      <td>70</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>41</td>
      <td>18</td>
      <td>24</td>
      <td>28</td>
      <td>70</td>
      <td>ARG</td>
    </tr>
    <tr>
      <th>Armenia</th>
      <td>5</td>
      <td>1</td>
      <td>2</td>
      <td>9</td>
      <td>12</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>1</td>
      <td>2</td>
      <td>9</td>
      <td>12</td>
      <td>ARM</td>
    </tr>
    <tr>
      <th>Australasia</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>12</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>12</td>
      <td>ANZ</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Question 1
# Which country has won the most gold medals in summer games?
df.Gold.max()
```




    976




```python
# Question 1.1
df[df['Gold'] == 976].index.tolist()
```




    ['United States']




```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># Summer</th>
      <th>Gold</th>
      <th>Silver</th>
      <th>Bronze</th>
      <th>Total</th>
      <th># Winter</th>
      <th>Gold.1</th>
      <th>Silver.1</th>
      <th>Bronze.1</th>
      <th>Total.1</th>
      <th># Games</th>
      <th>Gold.2</th>
      <th>Silver.2</th>
      <th>Bronze.2</th>
      <th>Combined total</th>
      <th>ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>AFG</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>12</td>
      <td>5</td>
      <td>2</td>
      <td>8</td>
      <td>15</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>5</td>
      <td>2</td>
      <td>8</td>
      <td>15</td>
      <td>ALG</td>
    </tr>
    <tr>
      <th>Argentina</th>
      <td>23</td>
      <td>18</td>
      <td>24</td>
      <td>28</td>
      <td>70</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>41</td>
      <td>18</td>
      <td>24</td>
      <td>28</td>
      <td>70</td>
      <td>ARG</td>
    </tr>
    <tr>
      <th>Armenia</th>
      <td>5</td>
      <td>1</td>
      <td>2</td>
      <td>9</td>
      <td>12</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>1</td>
      <td>2</td>
      <td>9</td>
      <td>12</td>
      <td>ARM</td>
    </tr>
    <tr>
      <th>Australasia</th>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>12</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>12</td>
      <td>ANZ</td>
    </tr>
    <tr>
      <th>Australia</th>
      <td>25</td>
      <td>139</td>
      <td>152</td>
      <td>177</td>
      <td>468</td>
      <td>18</td>
      <td>5</td>
      <td>3</td>
      <td>4</td>
      <td>12</td>
      <td>43</td>
      <td>144</td>
      <td>155</td>
      <td>181</td>
      <td>480</td>
      <td>AUS</td>
    </tr>
    <tr>
      <th>Austria</th>
      <td>26</td>
      <td>18</td>
      <td>33</td>
      <td>35</td>
      <td>86</td>
      <td>22</td>
      <td>59</td>
      <td>78</td>
      <td>81</td>
      <td>218</td>
      <td>48</td>
      <td>77</td>
      <td>111</td>
      <td>116</td>
      <td>304</td>
      <td>AUT</td>
    </tr>
    <tr>
      <th>Azerbaijan</th>
      <td>5</td>
      <td>6</td>
      <td>5</td>
      <td>15</td>
      <td>26</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>6</td>
      <td>5</td>
      <td>15</td>
      <td>26</td>
      <td>AZE</td>
    </tr>
    <tr>
      <th>Bahamas</th>
      <td>15</td>
      <td>5</td>
      <td>2</td>
      <td>5</td>
      <td>12</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>15</td>
      <td>5</td>
      <td>2</td>
      <td>5</td>
      <td>12</td>
      <td>BAH</td>
    </tr>
    <tr>
      <th>Bahrain</th>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>BRN</td>
    </tr>
    <tr>
      <th>Barbados</th>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>BAR</td>
    </tr>
    <tr>
      <th>Belarus</th>
      <td>5</td>
      <td>12</td>
      <td>24</td>
      <td>39</td>
      <td>75</td>
      <td>6</td>
      <td>6</td>
      <td>4</td>
      <td>5</td>
      <td>15</td>
      <td>11</td>
      <td>18</td>
      <td>28</td>
      <td>44</td>
      <td>90</td>
      <td>BLR</td>
    </tr>
    <tr>
      <th>Belgium</th>
      <td>25</td>
      <td>37</td>
      <td>52</td>
      <td>53</td>
      <td>142</td>
      <td>20</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>5</td>
      <td>45</td>
      <td>38</td>
      <td>53</td>
      <td>56</td>
      <td>147</td>
      <td>BEL</td>
    </tr>
    <tr>
      <th>Bermuda</th>
      <td>17</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>24</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>BER</td>
    </tr>
    <tr>
      <th>Bohemia</th>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>BOH</td>
    </tr>
    <tr>
      <th>Botswana</th>
      <td>9</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>BOT</td>
    </tr>
    <tr>
      <th>Brazil</th>
      <td>21</td>
      <td>23</td>
      <td>30</td>
      <td>55</td>
      <td>108</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>28</td>
      <td>23</td>
      <td>30</td>
      <td>55</td>
      <td>108</td>
      <td>BRA</td>
    </tr>
    <tr>
      <th>British West Indies</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>BWI</td>
    </tr>
    <tr>
      <th>Bulgaria</th>
      <td>19</td>
      <td>51</td>
      <td>85</td>
      <td>78</td>
      <td>214</td>
      <td>19</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>6</td>
      <td>38</td>
      <td>52</td>
      <td>87</td>
      <td>81</td>
      <td>220</td>
      <td>BUL</td>
    </tr>
    <tr>
      <th>Burundi</th>
      <td>5</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>BDI</td>
    </tr>
    <tr>
      <th>Cameroon</th>
      <td>13</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>14</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>CMR</td>
    </tr>
    <tr>
      <th>Canada</th>
      <td>25</td>
      <td>59</td>
      <td>99</td>
      <td>121</td>
      <td>279</td>
      <td>22</td>
      <td>62</td>
      <td>56</td>
      <td>52</td>
      <td>170</td>
      <td>47</td>
      <td>121</td>
      <td>155</td>
      <td>173</td>
      <td>449</td>
      <td>CAN</td>
    </tr>
    <tr>
      <th>Chile</th>
      <td>22</td>
      <td>2</td>
      <td>7</td>
      <td>4</td>
      <td>13</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>38</td>
      <td>2</td>
      <td>7</td>
      <td>4</td>
      <td>13</td>
      <td>CHI</td>
    </tr>
    <tr>
      <th>China</th>
      <td>9</td>
      <td>201</td>
      <td>146</td>
      <td>126</td>
      <td>473</td>
      <td>10</td>
      <td>12</td>
      <td>22</td>
      <td>19</td>
      <td>53</td>
      <td>19</td>
      <td>213</td>
      <td>168</td>
      <td>145</td>
      <td>526</td>
      <td>CHN</td>
    </tr>
    <tr>
      <th>Colombia</th>
      <td>18</td>
      <td>2</td>
      <td>6</td>
      <td>11</td>
      <td>19</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>19</td>
      <td>2</td>
      <td>6</td>
      <td>11</td>
      <td>19</td>
      <td>COL</td>
    </tr>
    <tr>
      <th>Costa Rica</th>
      <td>14</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>20</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>CRC</td>
    </tr>
    <tr>
      <th>Ivory Coast</th>
      <td>12</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>CIV</td>
    </tr>
    <tr>
      <th>Croatia</th>
      <td>6</td>
      <td>6</td>
      <td>7</td>
      <td>10</td>
      <td>23</td>
      <td>7</td>
      <td>4</td>
      <td>6</td>
      <td>1</td>
      <td>11</td>
      <td>13</td>
      <td>10</td>
      <td>13</td>
      <td>11</td>
      <td>34</td>
      <td>CRO</td>
    </tr>
    <tr>
      <th>Cuba</th>
      <td>19</td>
      <td>72</td>
      <td>67</td>
      <td>70</td>
      <td>209</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>19</td>
      <td>72</td>
      <td>67</td>
      <td>70</td>
      <td>209</td>
      <td>CUB</td>
    </tr>
    <tr>
      <th>Cyprus</th>
      <td>9</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>19</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>CYP</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Spain</th>
      <td>22</td>
      <td>37</td>
      <td>59</td>
      <td>35</td>
      <td>131</td>
      <td>19</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>41</td>
      <td>38</td>
      <td>59</td>
      <td>36</td>
      <td>133</td>
      <td>ESP</td>
    </tr>
    <tr>
      <th>Sri Lanka</th>
      <td>16</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>16</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>SRI</td>
    </tr>
    <tr>
      <th>Sudan</th>
      <td>11</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>SUD</td>
    </tr>
    <tr>
      <th>Suriname</th>
      <td>11</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>SUR</td>
    </tr>
    <tr>
      <th>Sweden</th>
      <td>26</td>
      <td>143</td>
      <td>164</td>
      <td>176</td>
      <td>483</td>
      <td>22</td>
      <td>50</td>
      <td>40</td>
      <td>54</td>
      <td>144</td>
      <td>48</td>
      <td>193</td>
      <td>204</td>
      <td>230</td>
      <td>627</td>
      <td>SWE</td>
    </tr>
    <tr>
      <th>Switzerland</th>
      <td>27</td>
      <td>47</td>
      <td>73</td>
      <td>65</td>
      <td>185</td>
      <td>22</td>
      <td>50</td>
      <td>40</td>
      <td>48</td>
      <td>138</td>
      <td>49</td>
      <td>97</td>
      <td>113</td>
      <td>113</td>
      <td>323</td>
      <td>SUI</td>
    </tr>
    <tr>
      <th>Syria</th>
      <td>12</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>SYR</td>
    </tr>
    <tr>
      <th>Chinese Taipei</th>
      <td>13</td>
      <td>2</td>
      <td>7</td>
      <td>12</td>
      <td>21</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>24</td>
      <td>2</td>
      <td>7</td>
      <td>12</td>
      <td>21</td>
      <td>TPE</td>
    </tr>
    <tr>
      <th>Tajikistan</th>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>TJK</td>
    </tr>
    <tr>
      <th>Tanzania</th>
      <td>12</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>TAN</td>
    </tr>
    <tr>
      <th>Thailand</th>
      <td>15</td>
      <td>7</td>
      <td>6</td>
      <td>11</td>
      <td>24</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>18</td>
      <td>7</td>
      <td>6</td>
      <td>11</td>
      <td>24</td>
      <td>THA</td>
    </tr>
    <tr>
      <th>Togo</th>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>TOG</td>
    </tr>
    <tr>
      <th>Tonga</th>
      <td>8</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>TGA</td>
    </tr>
    <tr>
      <th>Trinidad and Tobago</th>
      <td>16</td>
      <td>2</td>
      <td>5</td>
      <td>11</td>
      <td>18</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>19</td>
      <td>2</td>
      <td>5</td>
      <td>11</td>
      <td>18</td>
      <td>TRI</td>
    </tr>
    <tr>
      <th>Tunisia</th>
      <td>13</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>10</td>
      <td>TUN</td>
    </tr>
    <tr>
      <th>Turkey</th>
      <td>21</td>
      <td>39</td>
      <td>25</td>
      <td>24</td>
      <td>88</td>
      <td>16</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>37</td>
      <td>39</td>
      <td>25</td>
      <td>24</td>
      <td>88</td>
      <td>TUR</td>
    </tr>
    <tr>
      <th>Uganda</th>
      <td>14</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>14</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>7</td>
      <td>UGA</td>
    </tr>
    <tr>
      <th>Ukraine</th>
      <td>5</td>
      <td>33</td>
      <td>27</td>
      <td>55</td>
      <td>115</td>
      <td>6</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>7</td>
      <td>11</td>
      <td>35</td>
      <td>28</td>
      <td>59</td>
      <td>122</td>
      <td>UKR</td>
    </tr>
    <tr>
      <th>United Arab Emirates</th>
      <td>8</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>8</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>UAE</td>
    </tr>
    <tr>
      <th>United States</th>
      <td>26</td>
      <td>976</td>
      <td>757</td>
      <td>666</td>
      <td>2399</td>
      <td>22</td>
      <td>96</td>
      <td>102</td>
      <td>84</td>
      <td>282</td>
      <td>48</td>
      <td>1072</td>
      <td>859</td>
      <td>750</td>
      <td>2681</td>
      <td>USA</td>
    </tr>
    <tr>
      <th>Uruguay</th>
      <td>20</td>
      <td>2</td>
      <td>2</td>
      <td>6</td>
      <td>10</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>21</td>
      <td>2</td>
      <td>2</td>
      <td>6</td>
      <td>10</td>
      <td>URU</td>
    </tr>
    <tr>
      <th>Uzbekistan</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>10</td>
      <td>20</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>11</td>
      <td>6</td>
      <td>5</td>
      <td>10</td>
      <td>21</td>
      <td>UZB</td>
    </tr>
    <tr>
      <th>Venezuela</th>
      <td>17</td>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>12</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>21</td>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>12</td>
      <td>VEN</td>
    </tr>
    <tr>
      <th>Vietnam</th>
      <td>14</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>14</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>VIE</td>
    </tr>
    <tr>
      <th>Virgin Islands</th>
      <td>11</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>18</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>ISV</td>
    </tr>
    <tr>
      <th>Yugoslavia</th>
      <td>16</td>
      <td>26</td>
      <td>29</td>
      <td>28</td>
      <td>83</td>
      <td>14</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>4</td>
      <td>30</td>
      <td>26</td>
      <td>32</td>
      <td>29</td>
      <td>87</td>
      <td>YUG</td>
    </tr>
    <tr>
      <th>Independent Olympic Participants</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>IOP</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>12</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>ZAM</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>12</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>8</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>8</td>
      <td>ZIM</td>
    </tr>
    <tr>
      <th>Mixed team</th>
      <td>3</td>
      <td>8</td>
      <td>5</td>
      <td>4</td>
      <td>17</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>8</td>
      <td>5</td>
      <td>4</td>
      <td>17</td>
      <td>ZZX</td>
    </tr>
  </tbody>
</table>
<p>146 rows × 16 columns</p>
</div>




```python
# Question 2
# Which country had the biggest difference between their summer and winter gold medal counts?
df[['Gold', 'Gold.1']].head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gold</th>
      <th>Gold.1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Argentina</th>
      <td>18</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Armenia</th>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Australasia</th>
      <td>3</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
df.dtypes
#diff = (df[['Gold']] - (df[['Gold.1']])) 
```




    # Summer           int64
    Gold               int64
    Silver             int64
    Bronze             int64
    Total              int64
    # Winter           int64
    Gold.1             int64
    Silver.1           int64
    Bronze.1           int64
    Total.1            int64
    # Games            int64
    Gold.2             int64
    Silver.2           int64
    Bronze.2           int64
    Combined total     int64
    ID                object
    dtype: object




```python
# Question 2.1
#sub =  (df['Gold'].values - df['Gold.1'].values).max()
#- (df[['Gold.1'].values])
(df['Gold'].values) - (df['Gold.1'].values).max()
```




    array([-118, -113, -100, -117, -115,   21, -100, -112, -113, -118, -118,
           -106,  -81, -118, -118, -118,  -95, -118,  -67, -117, -115,  -59,
           -116,   83, -116, -117, -118, -112,  -46, -118, -104,  -69,  -75,
           -118, -115, -117, -111, -118, -109,  -97,  -17,   84, -118, -112,
             56,  -90,   35,  -62, -118,  118,  -88, -117, -118, -118, -118,
           -117,   49, -118, -109, -112, -103, -118, -109, -117,   80, -101,
             12, -102,  -93, -104,  -37, -118, -118, -115, -118, -118, -112,
           -117, -118, -118, -118, -105, -118, -116, -118, -112, -117, -118,
            -41, -118,  -76, -118, -115,  -62, -115, -117, -118, -117, -118,
            -54, -114, -118, -118,  -30,   14, -117,  277,  -73, -118, -118,
           -117, -116, -118, -111, -114,  -95,  -81, -118, -118, -117,   25,
            -71, -117, -116, -118, -118, -111, -118, -118, -116, -115,  -79,
           -116,  -85, -117,  858, -116, -113, -116, -118, -118,  -92, -118,
           -118, -115, -110])




```python
# Question 2.2
sub
```




    880




```python
# Question 2.3
#df.iloc[((df['Gold'].values - df['Gold.1'].values)) == sub, ].index.tolist()

df.iloc[((df['Gold'].values) - (df['Gold.1'].values)) == 880, ].index.tolist()
```




    ['United States']




```python
# Question 3 
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative
#to their total gold medal count?
# ((Summer Gold - Winter Gold) / Total Gold)
# Only include countries that have won at least 1 gold in both summer and winter.

totes = (((df['Gold'].values) - (df['Gold.1'].values)) / (df['Combined total'])).max()
```




    1.0




```python
# Burundi,  #Grenada and # United Emirates should be answer => value is one

df.loc[((((df['Gold'].values) - (df['Gold.1'].values)) / (df['Combined total'])) == 1.0)].index.tolist()
```




    ['Burundi', 'Grenada', 'United Arab Emirates']




```python
# Question 4
```
