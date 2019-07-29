#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 19:59:55 2019

@author: aritra
"""

import pandas as pd
weather_data={'date':['2019-07-01','2019-07-02','2019-07-03','2019-07-04','2019-07-05','2019-07-06'],
              'max_temp':[37,36,35,34,35,33],
              'min_temp':[27,26,28,23,28,22],
              'windspeed':[8,5,6,4,3,5],
              'event':['sunny','rainy','sunny','rainy','sunny','rainy']
              }
weather_df=pd.DataFrame(weather_data)
print(weather_df)