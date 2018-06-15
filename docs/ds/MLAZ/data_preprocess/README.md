
# Data preprocessing

This is the most important and sometimes boring step, but you gotta have to do it, since *a bad dataset would give bad results*. 

For starters, we would need to import the following libraries which are the most used and essential set of libraries. 

1. Numpy (used for N-dimensional array object)
2. Matplotlib (For plotting mathematical graphs)
3. Pandas (For dataframes that matter)


```python
# Importing libraries
import numpy as np
import matplotlib.pyplot
import pandas as pd

# Importing the dataset
# %pwd
dataset = pd.read_csv('datastore/Data.csv')

# We need to distinguish between the matrix of features and the dependent variable vector
X = dataset.iloc[:,:-1].values
# print(X)
Y = dataset.iloc[:,3].values
# print(Y)
# Previewing the dataset
dataset.head(10)
```




<div>
<!-- <style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }
    .dataframe tbody tr th {
        vertical-align: top;
    }
    .dataframe thead th {
        text-align: right;
    }
</style> -->
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Age</th>
      <th>Salary</th>
      <th>Purchased</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>France</td>
      <td>44.0</td>
      <td>72000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Spain</td>
      <td>27.0</td>
      <td>48000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Germany</td>
      <td>30.0</td>
      <td>54000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spain</td>
      <td>38.0</td>
      <td>61000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Germany</td>
      <td>40.0</td>
      <td>NaN</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>5</th>
      <td>France</td>
      <td>35.0</td>
      <td>58000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Spain</td>
      <td>NaN</td>
      <td>52000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>7</th>
      <td>France</td>
      <td>48.0</td>
      <td>79000.0</td>
      <td>Yes</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Germany</td>
      <td>50.0</td>
      <td>83000.0</td>
      <td>No</td>
    </tr>
    <tr>
      <th>9</th>
      <td>France</td>
      <td>37.0</td>
      <td>67000.0</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>
</div>



## Analysing the data `head`

> Note : The data cannot be analyzed using the `head` command, it just gives us a glimpse of the dataset.

**Observation** : We observe from the dataset that the data is unclean. We would need to clean the data from NaN( not a number )s.

To do this, there are 2 strategies :
1. To omit the tuples containing NaN in any column
2. To substitute them with the mean of the column data ( so as to not miss the tuple ).


```python
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy = 'mean',axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
print(X)
```

    [['France' 44.0 72000.0]
     ['Spain' 27.0 48000.0]
     ['Germany' 30.0 54000.0]
     ['Spain' 38.0 61000.0]
     ['Germany' 40.0 63777.77777777778]
     ['France' 35.0 58000.0]
     ['Spain' 38.77777777777778 52000.0]
     ['France' 48.0 79000.0]
     ['Germany' 50.0 83000.0]
     ['France' 37.0 67000.0]]
    
