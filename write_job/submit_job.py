#!/usr/bin/env python
#import numpy as np
#import pandas as pd
#import os,sys,time

import os

i1 = 0
step = 1
i2 = i1 + int(step*3)

for i in range(i1,i2,step):
#print(i)
    command_line = "qsub job_%s.sh &"%(i)
    print(command_line)
    os.system(command_line)
