import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn.linear_model import LinearRegression as LinReg

#tables = pd.read_html("http://apps.sandiego.gov/sdfiredispatch/")
#print(tables[0])
#fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states', flavor='html5lib`)
#print(len(tables))

# create a series
#pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
#s = pd.Series(np.random.randn(5))

s = pd.Series([1,3,4,5,-1])

print(s)

print(s[0])
print('\n')
print(s[:3])

# DataFrames
# 2 dimensional tabular data structure
# capatable of holding any/many data types
# index and columns

# Create a dataframe
df = pd.DataFrame(s, columns = ['Column 1'])
print(df)

# Can access columns by name
print(df['Column 1'])

# Easy to add columns
df['Column 2'] = df['Column 1'] * 4
print(df)

# Other manipulation, like sorting -- if you want to preserve, set equal to a var
df = df.sort_values(by = 'Column 2')
print(df)

#Boolean indexing
df = df[df['Column 2'] <=15]
print(df)

b= df.apply(lambda x: min(x)+max(x))
print(b)

c = np.mean(df)
print(c)

d = df.describe()
print(d)

#df_av = d["mean"] ???
#print(df_av)

##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### How have Earth surface temperatures changed over time?
#https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data

# Read in data into a dataframe
df = pd.read_csv('GlobalTemperatures.csv')

# Show the first 30 rows and the last 30 rows of the table
print(df.head)
print(df.tail(5))

# Let's just consider the LandAverageTemperatures
# A primarily label-location based indexer

df = df.ix[:,:2]
print(df.head())

print(df.describe())

# Cursory plot
plt.figure(figsize = (15,5))
plt.plot(df['LandAverageTemperature'])
plt.title('Average Temperature')
plt.xlabel('Year')
plt.ylabel('Temperature')
#plt.show()

plt.figure(figsize = (15,5))
plt.scatter(x=df['LandAverageTemperature'].index, y = df['LandAverageTemperature'])
plt.title('Average Temperature')
plt.xlabel('Year')
plt.ylabel('Temperature')
#plt.show()


#Maybe we can try only by year?
# But notice that the dt column is made up of strings
print(type(df['dt'][0]))

# Convert to datetime object
times = pd.DatetimeIndex(df['dt'])
print(type(times))

# Group by year
grouped = df.groupby([times.year]).mean()
# Plot
plt.figure(figsize=(15,5))
plt.plot(grouped['LandAverageTemperature'])
plt.title('Average Temperature')
plt.xlabel('Year')
plt.ylabel('Temperature')
#plt.show()

# What caused those anomalies?
print(grouped.head())

# Check what happened in 1752
print(df[times.year == 1752])

# There are a lot of null values
print(df[np.isnan(df['LandAverageTemperature'])])

# Use previous valid observation to fill gap
df['LandAverageTemperature'] = df['LandAverageTemperature'].fillna(method = 'ffill')

# Regroup and plot
grouped = df.groupby([times.year]).mean()
# Plot
plt.figure(figsize=(15,5))
plt.plot(grouped['LandAverageTemperature'])
plt.title('Average Temperature-filled')
plt.xlabel('Year')
plt.ylabel('Temperature')
#plt.show()

# Better but still not perfect
# What are some other ways to fill the NaN values?


##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Modeling a dataset

x = grouped.index.values.reshape(-1,1)
y = grouped['LandAverageTemperature'].values

reg = LinReg()
reg.fit(x,y)
y_preds = reg.predict(x)
print('Accuracy:' + str(reg.score(x,y)))

plt.figure(figsize=(15,5))
plt.title('Average Temperature')
plt.scatter(x = x, y=y_preds)
plt.scatter(x = x, y=y, c = "r")
#plt.show()

# predicted value at x = 2050
print(reg.predict(2050))

## Data Resources:
# Havard Open Data Project
# Kaggle
# data.gov, data.cityofboston.gov
# Data Ventures, CS109a/b, CS181


## Some projects
# Predicting NBA draft order