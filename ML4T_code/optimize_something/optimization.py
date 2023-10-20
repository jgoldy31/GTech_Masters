""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""MC1-P2: Optimize a portfolio.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd  		  	   		  		 		  		  		    	 		 		   		 		  
from util import get_data, plot_data
import scipy.optimize as spo
from scipy.optimize import NonlinearConstraint
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		  	   		  		 		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality
def f_sharpe(allocs, dr):
    daily_rets = dr[1:]
    avg_daily_ret = (daily_rets * allocs).sum(axis=1).mean()
    std_daily_ret = (daily_rets * allocs).sum(axis=1).std()
    daily_rf = 0.0
    sharpe = math.sqrt(252) * (avg_daily_ret - daily_rf)/ std_daily_ret
    return -sharpe



def compute_daily_ret(df):
    dr = df.copy()
    dr[1:] = (df[1:]/df[:-1].values) - 1
    dr.ix[0,:] - 0
    return dr

# Define the custom equality constraint function
def sum_check(vals):
    return 1.0 - np.sum(vals)

def optimize_portfolio(  		  	   		  		 		  		  		    	 		 		   		 		  
    sd=dt.datetime(2008, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
    ed=dt.datetime(2009, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		  		 		  		  		    	 		 		   		 		  
    gen_plot=True,
):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		  		 		  		  		    	 		 		   		 		  
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		  		 		  		  		    	 		 		   		 		  
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		  		 		  		  		    	 		 		   		 		  
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		  		 		  		  		    	 		 		   		 		  
    statistics.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  		 		  		  		    	 		 		   		 		  
    :type sd: datetime  		  	   		  		 		  		  		    	 		 		   		 		  
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  		 		  		  		    	 		 		   		 		  
    :type ed: datetime  		  	   		  		 		  		  		    	 		 		   		 		  
    :param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		  		 		  		  		    	 		 		   		 		  
        symbol in the data directory)  		  	   		  		 		  		  		    	 		 		   		 		  
    :type syms: list  		  	   		  		 		  		  		    	 		 		   		 		  
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		  		 		  		  		    	 		 		   		 		  
        code with gen_plot = False.  		  	   		  		 		  		  		    	 		 		   		 		  
    :type gen_plot: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		  		 		  		  		    	 		 		   		 		  
        standard deviation of daily returns, and Sharpe ratio  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: tuple  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # Read in adjusted closing prices for given symbols, date range  		  	   		  		 		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		  	   		  		 		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY  		  	   		  		 		  		  		    	 		 		   		 		  
    prices = prices_all[syms]  # only portfolio symbols  		  	   		  		 		  		  		    	 		 		   		 		  
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		  		 		  		  		    	 		 		   		 		  

    #First step get the normalized price values
    normed = prices / prices.values[0]
    daily_ret = compute_daily_ret(prices)
    #Now start making paramters for scipy minimize
    #first guess will just be everything equal
    guess_number = 1/len(syms)
    starting_guess = np.repeat(guess_number,len(syms))
    #define constraints
    these_bounds =  [(0.,1.)for i in range(len(syms))]
    these_constraints = ({ 'type': 'ineq', 'fun': lambda inputs: 1.0 - np.sum(inputs) },
                         { 'type': 'ineq', 'fun': lambda inputs: np.sum(inputs) - 1.0}
                         )
    # find the allocations for the optimal portfolio
    min_res = spo.minimize(f_sharpe,starting_guess,args = (daily_ret,), method = 'SLSQP',constraints = these_constraints,bounds = these_bounds,options={'disp': True})
    # note that the values here ARE NOT meant to be correct for a test case
    allocs = min_res.x # add code here to find the allocations
    print(allocs)
    print(sum(allocs))
    alloced = normed * allocs
    pos_vals = alloced * 100
    port_val = pos_vals.sum(axis=1)
    # Sharpe ratio
    cr = (port_val[-1] / port_val[0] - 1)
    adr = (daily_ret * allocs).sum(axis=1).mean()
    sddr = (daily_ret * allocs).sum(axis=1).std()
    sr = math.sqrt(252) * adr/sddr
    # cr, adr, sddr, sr = [
    #     cr,
    #     avg_daily_ret,
    #     std_daily_ret,
    #     sharpe
    # ]  # add code here to compute stats
  		  	   		  		 		  		  		    	 		 		   		 		  
    # Compare daily portfolio value with SPY using a normalized plot  		  	   		  		 		  		  		    	 		 		   		 		  
    if gen_plot:
        port_norm = port_val/port_val[0]
        spy_norm = prices_SPY/prices_SPY[0]
        plt.plot(port_norm, color='blue', label='Portfolio')
        plt.plot( spy_norm, color='green', label='SPY')
        plt.title('Daily Portfolio Value and SPY')
        plt.ylabel('Price')
        plt.xlabel('Date')
        plt.legend()
        figure_1 = plt.gcf()
        figure_1.savefig('images/chart.png')

        pass  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    return allocs, cr, adr, sddr, sr

def str2dt(strng):
    year, month, day = map(int, strng.split("-"))
    return dt.datetime(year, month, day)
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def test_code():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    This function WILL NOT be called by the auto grader.  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2009, 1, 1)  		  	   		  		 		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2010, 1, 1)  		  	   		  		 		  		  		    	 		 		   		 		  
    symbols = ["GOOG", "AAPL", "GLD", "XOM", "IBM"]
    # Assess the portfolio  		  	   		  		 		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		  		 		  		  		    	 		 		   		 		  
        sd=start_date, ed=end_date, syms=symbols, gen_plot=True
    )  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # Print statistics  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Symbols: {symbols}")
    print(f"Allocations:{allocations}")
    print(f"Sharpe Ratio: {sr}")
    print(f"Volatility (stdev of daily returns): {sddr}")
    print(f"Average Daily Return: {adr}")
    print(f"Cumulative Return: {cr}")
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		  	   		  		 		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		  	   		  		 		  		  		    	 		 		   		 		  
    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  
