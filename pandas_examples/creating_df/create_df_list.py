# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:15:37 2019

@author: aritra
"""

import pandas as pd
weather_data=[{'day':'2019-07-01','max_temp':37,'min_temp':27,'windspeed':8,'event':'sunny'}, {'day':'2019-07-02','max_temp':35,'min_temp':23,'windspeed':5,'event':'rainy'},{'day':'2019-07-03','max_temp':36,'min_temp':25,'windspeed':6,'event':'sunny'}]
weather_df=pd.DataFrame(weather_data)
print(weather_df)