"""
Student Name: Jenny Goldsher		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: jgoldsher3  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903848300  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from util import *
import TheoreticallyOptimalStrategy as ts
from indicators import *
  		  	   		  		 		  		  		    	 		 		   		 		  

  		  	   		  		 		  		  		    	 		 		   		 		  
def author():
    return "jgoldsher3"


def compute_portvals(
        orders_file,
        start_val=1000000,
        commission=9.95,
        impact=0.005,
):
    # this is the function the autograder will call to test your code
    # NOTE: orders_file may be a string, or it may be a file object. Your
    # code should work correctly with either input
    data =orders_file
    commission = 9.95
    start_val = 1000000
    impact = .005
    data.index = pd.to_datetime(data.index)
    start_date = data.index.min()
    end_date = data.index.max()
    df_prices = get_data(data['Symbol'].unique(), pd.date_range(start_date, end_date))
    # drop SPY
    df_prices.drop('SPY', axis=1, inplace=True)
    df_prices['Cash'] = 1

    # make empty trades df with all values at 0
    df_trades = df_prices.copy()
    df_trades.iloc[:, :] = 0
    # make empty holdings df with all values at 0 except cash
    df_holdings = df_prices.copy()
    df_holdings.iloc[:, :] = 0


    # trades
    for i in range(len(data)):
        this_order = data.iloc[i]
        this_date = pd.to_datetime(this_order.name)
        stock = this_order['Symbol']
        shares = this_order['Shares']
        order_type = this_order['Order']
        price_at_day = df_prices.loc[this_date, stock]
        pos_neg = 1
        if order_type == 'BUY':
            pos_neg = -1

        df_trades.loc[this_date, stock] += shares * -(pos_neg)
        fees = shares * price_at_day * impact
        df_trades.loc[this_date, 'Cash'] += shares * price_at_day * pos_neg - commission - fees

    # holdings, first row then loop
    this_order = data.iloc[0]
    this_date = pd.to_datetime(this_order.name)
    df_holdings.iloc[0] = df_trades.iloc[0]
    df_holdings.at[this_date, 'Cash'] += start_val

    for j in range(1, len(df_holdings)):
        row_val = df_holdings.iloc[j - 1].values + df_trades.iloc[j].values
        df_holdings.iloc[j] = row_val
    # compute portfolio values
    df_values = df_prices * df_holdings
    port_values = df_values.sum(axis=1)

    return port_values

if __name__ == "__main__":
    #Part 1: Theorhetical Optimal Strategy
    data = ts.testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000)
    df_trades = pd.DataFrame(index=data.index.values, columns=["Symbol", "Order", "Shares"])
    df_trades["Symbol"] = "JPM"
    df_trades["Order"] = data['in_portfolio'].apply(lambda x: 'BUY' if x > 0 else 'SELL')
    df_trades["Shares"] = abs(data['in_portfolio'])

    port_val = compute_portvals(df_trades)
    port_val = port_val / port_val.iloc[0]
    plot_dat = get_data(["JPM"], pd.date_range(dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31)),
                              colname="Adj Close")
    plot_dat = plot_dat[['JPM']] * 1000
    #compute
    plot_dat["benchmark"] = plot_dat / plot_dat.iloc[0]
    #add in already computed daily porfolio value
    plot_dat["p_val"] = port_val

    #plot how we did compared to benchmark
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(plot_dat.index, plot_dat['p_val'], label="Portfolio Value", color='red')
    ax.plot(plot_dat.index, plot_dat['benchmark'], label="Benchmark", color='purple')
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.set_title("Portfolio Value and Benchmark Value")
    ax.legend()
    figure_1 = plt.gcf()
    figure_1.savefig('bench_port.png')


    #table
    returns = plot_dat['benchmark'].diff()
    #benchmark
    b_cr = round(returns.sum(), 6)
    b_ar = round(returns.mean(), 6)
    b_std = round(returns.std(), 6)
    #port
    returns = plot_dat['p_val'].diff()
    p_cr = round(returns.sum(), 6)
    p_ar = round(returns.mean(), 6)
    p_std = round(returns.std(), 6)

    df = {
        'Measure': ['Cumulative Return', 'Average Daily Return', 'Standard Deviation (Daily)'],
        'Benchmark': [b_cr, b_ar, b_std],
        'Portfolio': [p_cr, p_ar, p_std]
    }

    df = pd.DataFrame(df)
    df.to_csv('p6_results.txt', index=False)

    #Part 2 --- Indicators
    adj_close = get_data(["JPM"], pd.date_range(dt.datetime(2008, 1, 1), dt.datetime(2009, 12, 31)),
                         colname="Adj Close")
    ema = EMA(adj_close['JPM']).dropna()
    sma = SMA(adj_close['JPM']).dropna()
    std = adj_close['JPM'].rolling(window=10).std()
    dat = (adj_close['JPM'] - sma).dropna()
    bbl, bbh = BB(adj_close['JPM'], sma, std)
    momentum = mom(adj_close['JPM']).dropna()
    ppo = PPO(adj_close['JPM'])

    plt.clf()
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

    plt.tight_layout()
    figure_2 = plt.gcf()
    figure_2.savefig('indicators.png')