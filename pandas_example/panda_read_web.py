import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import html5lib
import requests
plt.style.use('ggplot')
from sklearn.linear_model import LinearRegression as LinReg

#tables = pd.read_html("http://apps.sandiego.gov/sdfiredispatch/")
#print(tables[0])
s = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# s = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states', flavor='html5lib`)

#https://hhs-opioid-codeathon.data.socrata.com/resource/vcp5-amce.json

r = requests.get('https://hhs-opioid-codeathon.data.socrata.com/resource/vcp5-amce') #.json
x = r.json()
df = pd.read_json(x)
print df


#print(len(s))
#print(s)

#r = requests.get('http://api.football-data.org/v1/competitions/398/teams')
#x = r.json()
#df = pd.read_json(x)
#print df
