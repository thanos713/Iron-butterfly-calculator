import datetime as dt
import pandas as pd
import pandas_datareader.data as web
from statistics import mean

from plot import *

class Options(object):    
    def __call(self, S, K, ls, cost):
        return ls*(max([S-K,0.])-cost)

    def __put(self, S, K, ls, cost):
        return ls*(max([K-S,0.])-cost)
    
    def iron_butterfly(self, S):
        return 100*(self.__put(S,self.short_strikes,-1, self.cost_short_put) +
            self.__call(S, self.short_strikes,-1, self.cost_short_call) +
            self.__put(S,self.short_strikes-self.spread,1, self.cost_long_put) +
            self.__call(S,self.short_strikes + self.spread,1, self.cost_long_call))

    
    def __init__(self, ticker, curr_price, short_strikes, spread, cost_long_call, cost_long_put, cost_short_call, cost_short_put):
        self.short_strikes = short_strikes
        self.spread = spread
        self.cost_long_call = cost_long_call
        self.cost_long_put = cost_long_put
        self.cost_short_call = cost_short_call
        self.cost_short_put = cost_short_put
        self.curr_price = curr_price
        self.ticker = ticker
        
    def generate_historical_data(self):
        start = dt.datetime(2017,1,1) #Arbitrarily old
        end = dt.datetime.now()
        df = web.DataReader(self.ticker, 'yahoo', start, end) # Example for IEF
        df.index = pd.to_datetime(df.index).day_name()
        df = df.drop(columns=['High', 'Low', 'Adj Close', 'Volume'])   
        
        percs = [] #Percentages
        
        for idx in range(0,len(df)-10): #10: 2 weeks, Friday to Friday (dropping "unusual" weeks)
            if df.index[idx] == 'Friday':
                if df.index[idx+10] == 'Friday': #Generate % difference
                    percs.append((df.iloc[idx+10]['Close']-df.iloc[idx]['Open'])*100/df.iloc[idx]['Open'])
                    
        stock_prices = [] # Generate prices using the historical percentages and the current price
        [stock_prices.append(self.curr_price*(100+perc)/100) for perc in percs]
        
        return stock_prices
    
    def visual_iron_butterfly(self):
        N = 10000 #Number of points for visualization
        dt = 4.0*self.spread/N
        prices = []
        [prices.append(self.short_strikes-2.0*self.spread +i*dt) for i in range(0,N+1)]
        vals = []
        [vals.append(self.iron_butterfly(price)) for price in prices]
        
        make_pnl_plot(prices,vals)
    
        print("Max profit: " + str(round(max(vals),2)) + " at " + str(self.short_strikes) + ".")
        print("Max loss: " + str(round(min(vals),2)) + " beyond " + 
              str(self.short_strikes+self.spread) + " or " + str(self.short_strikes-self.spread) + ".")
        print("See fig.1 for more details.")
 


    def compute_prob(self):
        stock_prices = self.generate_historical_data()
        historical_pnl = []
        [historical_pnl.append(self.iron_butterfly(price)) for price in stock_prices]
    
        make_histogram(self, historical_pnl)
      
        exp_util = mean(historical_pnl)
        print("Expected utiliy (assuming no slippage and transaction costs): " + str(round(exp_util,2)) + ".")
        print("See fig.2 for more details.")