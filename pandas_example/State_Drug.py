import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = 'State_Drug_Utilization_Data_2013.csv'

a = pd.read_csv(filname, sep="\s+", header=None)
print(a.shape)

