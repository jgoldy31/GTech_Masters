""""
Student Name: Jenny Goldsher		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: jgoldsher3  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903848300  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		  		 		  		  		    	 		 		   		 		  
import os  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		  		 		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def compute_portvals(  		  	   		  		 		  		  		    	 		 		   		 		  
    orders_file="./orders/orders.csv",  		  	   		  		 		  		  		    	 		 		   		 		  
    start_val=1000000,  		  	   		  		 		  		  		    	 		 		   		 		  
    commission=9.95,  		  	   		  		 		  		  		    	 		 		   		 		  
    impact=0.005,  		  	   		  		 		  		  		    	 		 		   		 		  
):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Computes the portfolio values.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param orders_file: Path of the order file or the file object  		  	   		  		 		  		  		    	 		 		   		 		  
    :type orders_file: str or file object  		  	   		  		 		  		  		    	 		 		   		 		  
    :param start_val: The starting value of the portfolio  		  	   		  		 		  		  		    	 		 		   		 		  
    :type start_val: int  		  	   		  		 		  		  		    	 		 		   		 		  
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		  		 		  		  		    	 		 		   		 		  
    :type commission: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		  		 		  		  		    	 		 		   		 		  
    :type impact: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: pandas.DataFrame  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    # this is the function the autograder will call to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		  		 		  		  		    	 		 		   		 		  
    # code should work correctly with either input
    data = pd.read_csv(orders_file, parse_dates=True,index_col='Date',  na_values=['nan']).sort_index()
    data.index = pd.to_datetime(data.index)
    start_date = data.index.min()
    end_date = data.index.max()
    df_prices= get_data(data['Symbol'].unique(), pd.date_range(start_date, end_date))
    #drop SPY
    df_prices.drop('SPY', axis=1, inplace=True)
    df_prices['Cash'] = 1

    #make empty trades df with all values at 0
    df_trades = df_prices.copy()
    df_trades.iloc[:, :] = 0
    # make empty holdings df with all values at 0 except cash
    df_holdings = df_prices.copy()
    df_holdings.iloc[:, :] = 0

    #trades
    for i in range(len(data)):
        this_order = data.iloc[i]
        this_date = pd.to_datetime(this_order.name)
        stock = this_order['Symbol']
        shares = this_order['Shares']
        order_type = this_order['Order']
        price_at_day = df_prices.loc[this_date,stock]
        pos_neg = 1
        if order_type == 'BUY':
            pos_neg = -1

        df_trades.loc[this_date, stock] += shares * -(pos_neg)
        fees = shares * price_at_day * impact
        df_trades.loc[this_date, 'Cash'] += shares * price_at_day * pos_neg - commission - fees




    #holdings, first row then loop
    this_order = data.iloc[0]
    this_date = pd.to_datetime(this_order.name)
    df_holdings.iloc[0] = df_trades.iloc[0]
    df_holdings.at[this_date, 'Cash'] += start_val

    for j in range(1, len(df_holdings)):
        row_val = df_holdings.iloc[j - 1].values + df_trades.iloc[j].values
        df_holdings.iloc[j] = row_val
    #compute portfolio values
    df_values = df_prices*df_holdings
    port_values = df_values.sum(axis=1)



    return port_values
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():
    return "jgoldsher3"

def testPolicy(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011, 12, 31), sv=100000):
      df_prices= get_data([symbol], pd.date_range(sd, ed))
      df_prices.drop('SPY', axis=1, inplace=True)
      df_prices['change'] = df_prices.diff()
      df_prices['buy_sell'] = df_prices['change'].apply(lambda x: 'BUY' if x > 0 else 'SELL')
      df_prices['buy_sell'] = df_prices['buy_sell'].shift(-1)


      #make blank trades df
      df_trades = pd.DataFrame(columns=["in_portfolio"], index=df_prices.index.values)
      df_trades.iloc[:, :] = 0.0

      for i in range(len(df_trades)):
          this_order = df_trades.iloc[i]
          this_date = pd.to_datetime(this_order.name)
          signal = df_prices.loc[this_date, 'buy_sell']
          pos_neg = -1
          if signal == 'BUY':
              pos_neg = 1

          df_trades.loc[this_date, 'in_portfolio'] += 1000 * (pos_neg)

          if i + 1 < len(df_trades):
              this_order = df_trades.iloc[i + 1]
              this_date = pd.to_datetime(this_order.name)
              df_trades.loc[this_date, 'in_portfolio'] -= 1000 * (pos_neg)


      return df_trades
  		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    print(testPolicy())
