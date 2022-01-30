from plot import *
from Options import *

# Specify the parameters of the iron butterfly spread
option = Options(ticker='IEF', 
                 curr_price=112.59,
                 short_strikes=112.5, 
                 spread=1.0, 
                 cost_long_call=0.22, 
                 cost_long_put=0.24,
                 cost_short_call=0.62, 
                 cost_short_put=0.62) 

option.visual_iron_butterfly() # Plot the P/L curve at expiration
option.compute_prob() # Compute the expected utility and the histogram of the P/L
