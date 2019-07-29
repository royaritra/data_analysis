#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:08:10 2019

@author: aritra
"""

import pandas as pd
weather_data={('2019-07-01',37,27,8,'sunny'),('2019-07-02',36,26,5,'rainy'),('2019-07-03',35,28,6,'sunny')}
weather_df=pd.DataFrame(weather_data,columns=['date','max_temp','min_temp','wind_speed','event'])
print(weather_df)