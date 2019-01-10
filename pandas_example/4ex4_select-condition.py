import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'W0.txt'
#a=np.loadtxt(filename,unpack=True)
#a=np.genfromtxt(filename,unpack=True)

a = pd.read_csv('W0.txt', sep="\s+", header=None)
print(a.shape)
print(a.head)
a.columns = ["I","J","W"]
print(a.head)

# Select condition
a = a[a.I<5]
a = a[a.J<5]

print(a)

# Missing values
print(a[a.W.isnull()])

# Use average value
print(a.W.mean())
W_av = a.W.mean()
a.W = a.W.fillna(value = W_av)

print(a)
