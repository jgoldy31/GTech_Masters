"""
Student Name: Jenny Goldsher		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: jgoldsher3  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903848300  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		  		 		  		  		    	 		 		   		 		  
import os  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt
import pandas as pd  		  	   		  		 		  		  		    	 		 		   		 		  
from util import *


def author():
    return "jgoldsher3"
def EMA(df, lag=25):
    return df.ewm(span=lag).mean()
def SMA(df, win = 15):
    return df.rolling(window =win).mean()
def BB(df,sma, std):
    bb_value_low = (df - sma) - (2 * std)
    bb_value_high = (df - sma) + (2 * std)
    return bb_value_low, bb_value_high
def mom(df, window=15):
    return (df / df.shift(window)) - 1

def PPO(df, short=15, long=30):
    return 100 * (df.ewm(span=short, adjust=False).mean() - df.ewm(span=long, adjust=False).mean()) / df.ewm(span=long, adjust=False).mean()

if __name__ == "__main__":
    adj_close = get_data(["JPM"], pd.date_range(dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31)),
                              colname="Adj Close")
    ema = EMA(adj_close['JPM']).dropna()
    sma = SMA(adj_close['JPM']).dropna()
    std = adj_close['JPM'].rolling(window=10).std()
    dat = (adj_close['JPM'] - sma).dropna()
    bbl, bbh = BB(adj_close['JPM'],sma,std)
    momentum = mom(adj_close['JPM']).dropna()
    ppo = PPO(adj_close['JPM'])


    fig, axes = plt.subplots(3, 2, figsize=(16, 12))

    axes[0, 0].plot(ema, label='EMA', color='red')
    axes[0, 0].set_title('Exponential Moving Average (EMA)')

    axes[0, 1].plot(sma, label='SMA', color='blue')
    axes[0, 1].set_title('Simple Moving  (SMA)')

    axes[1, 0].plot(sma.index, dat, label='', color='black')
    axes[1, 0].plot(bbh.index, bbh, label='', color='red', linestyle='--')
    axes[1, 0].plot(bbl.index, bbl, label='', color='red', linestyle='--')

    axes[1, 0].set_title('Bollinger Bands')

    axes[1, 1].plot(momentum, label='Momentum', color='orange')
    axes[1, 1].set_title('Momentum')
    axes[2, 0].plot(ppo, label='PPO', color='green')
    axes[2, 0].set_title('PPO')

    plt.tight_layout()

