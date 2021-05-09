#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 00:03:58 2021

@author: vishakha
"""
import pandas as pd
import matplotlib.pyplot as plt

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