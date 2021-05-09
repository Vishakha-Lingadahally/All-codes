#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:33:12 2021

@author: vishakha
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

col_list=["Percent of freshmen receiving federal, state, local or institutional grant aid"]
col_list1=["Percent of total enrollment that are women"]
df=pd.read_csv("IPEDS_data.csv", usecols=col_list)
dg=pd.read_csv("IPEDS_data.csv", usecols=col_list1)
print(df["Percent of freshmen receiving federal, state, local or institutional grant aid"])
print(dg["Percent of total enrollment that are women"])

for col in df.columns:
    plt.scatter(df["Percent of freshmen receiving federal, state, local or institutional grant aid"], dg["Percent of total enrollment that are women"], label=col)
    plt.legend(loc='best', fontsize=16)
    plt.xlabel("Percent of freshmen receiving federal, state, local or institutional grant aid")
    plt.ylabel('Percent of total enrollment that are women')
    plt.show()

df.dropna(axis=0, how='all', inplace=True)
dg.dropna(axis=0, how='all', inplace=True)
stat, p = pearsonr(df["Percent of freshmen receiving federal, state, local or institutional grant aid"], dg["Percent of total enrollment that are women"])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')
