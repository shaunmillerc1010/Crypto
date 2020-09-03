#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:38:15 2020

@author: Shaun Miller

Here we design a program to display closing prices of selected currencies
with perdiod of 1 month and 5 minute intervals.
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

cl_price = pd.DataFrame()
currencys = ['LTC-USD', 'DASH-USD', 'ZEC-USD']
ohlcv_data = {}

for tick in currencys: 
    #ohlcv_data[tick] = yf.download(tick, period = '1mo', interval = '5m')
    ohlcv_data[tick] = yf.download(tick, period = '1mo', interval = '5m')
#data = yf.download('MSFT', period = '1mo', interval = '5m' )

for tick in currencys: cl_price[tick] = ohlcv_data[tick]['Adj Close']

cl_price.fillna(method='ffill', inplace = True) #fills NAN forward

cl_price.plot()

