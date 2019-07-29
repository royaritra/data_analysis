#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 22:37:45 2019

@author: aritra
"""

import pandas as pd
def convert_event(cell):
    if cell=="n.a":
        return 'sunny'
    return cell
def convert_max_temp(cell):
    if cell=="n.a":
        return 35
    return cell
df=pd.read_csv("/home/aritra/data_analysis/database/student_1.csv",header=None,names=["first_name","last_name","section","roll","blood_group","marks"]) #if we wat to make any particular rowas header, put header=row_number, if you want to skip 1st row, skiprow=1
print(df)
df_2=pd.read_csv("/home/aritra/data_analysis/database/student_1.csv",header=None,names=["first_name","last_name","section","roll","blood_group","marks"],nrows=2) #willprint the top 3 rows only
print(df_2)
df_3=pd.read_csv("/home/aritra/data_analysis/database/student_1.csv",header=None,names=["first_name","last_name","section","roll","blood_group","marks"],na_values=['not available','n.a']) #will replace the not available or n.a to NaN, useful for cleaning data
print(df_3)
df_4=pd.read_csv("/home/aritra/data_analysis/database/student_1.csv",header=None,names=["first_name","last_name","section","roll","blood_group","marks"],na_values={'roll':[-1,'not available','n.a'],'marks':[-1,104,'not available','n.a'],'blood_group':['not available','n.a']}) #will replace -1 to naN in roll but in marks, beside -1, 104 will also be converted to NaN 
print(df_4)
df_4.to_csv('new.csv',columns=['first_name','roll'])#will write the df_4 to a new csv file with indexes, if dont want index, write index=False , columns argumet helps to selectively print some columns 
df_5=pd.read_excel("/home/aritra/data_analysis/database/weather_1_excel.xlsx","Sheet1",converters={
        'max_temp':convert_max_temp,
        'event': convert_event
        })
df_5.to_excel("new_2.xlsx", sheet_name='weather',startrow=3,startcol=2,index=False)
