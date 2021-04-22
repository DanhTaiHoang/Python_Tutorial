#!/usr/bin/env python
#import numpy as np
#import pandas as pd
#import os,sys,time


##===========================================================
a = ["#!/bin/bash \n"
     "#PBS -l ncpus=2 \n",
     "#PBS -l ngpus=0 \n",
     "#PBS -l mem=1GB \n",
     "#PBS -l jobfs=0GB \n",
     "#PBS -l walltime=0:02:00\n",
     "##PBS -q normal \n",
     "#PBS -q gpuvolta \n",
     "#PBS -P xd23 \n",
     "#PBS -l storage=scratch/dl76+scratch/xd23 \n",
     "#PBS -l wd \n",
     "module load python3/3.8.5 \n"]

##===========================================================
for i in range(4):
     f = open("job_%s.sh"%i ,"w")
     f.writelines(a)
     f.write("python3 test.py %s >$PBS_JOBID.log" %i)
     f.close()

