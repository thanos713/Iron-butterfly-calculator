# Iron-butterfly calculator

Iron-butterfly calculator is a software, written in Python, for computing, using historical data from yahoo finance, the probability and expected value of profiting from selling iron-butterfly spreads with 2 weeks from expiration (from Friday to Friday). The motivation was to use this strategy for intermediate to long term treasury bonds, as their price has very low volatility compared to most of the assets, but unfortunately I have not been able to backtest it explicitly, due to lack of historical data for options. Instead, Iron-butterfly calculator does the "opposite"; it gets current market data (from the user) to predict if the strategy will be profitable or not, by using historical data.

- To do that, the software computes 2-week changes in the price of the underlying (as a percentage) using historical data and then use them as a distribution for the future price of the underlying asset in 2 weeks from "now".

It is important to note that this process has its limitations, because of its assumptions. More specifically:
	1) The present code only works for 2-week horizons and from Friday to Friday (although it is trivial to change it). This is more of a feature than a limitation, though, because it is trivial to change.
	2) On the other hand, all the calculations are taken at expiration, even though the options used for the strategy are American and not European. This can be a significant risk in the case of assignment.
	3) No transactions costs are taken into account, which in practice cannot be neglected as the options can be highly illiquid (especially on bond ETFs such as IEF).
	4) No dividends are explicitly taken into account, although some of their effects are already present the historical data (via a drop in price). This can also come into play when considering early assignment.

---

## Files

*  **main.py** is the driver code. Changing the ticker (in the example 'IEF') to another ETF or stock, should immediately give you the new results, provided that you also change the current price of the asset, the strike prices of the "short" legs, the spread of the iron butterfly and the costs of each of the 4 options. By "spread", we denote the absolute difference in strike prices between the "short" and the "long" legs (assuming that the calls and the puts have the same spread).
*  **plot.py** contains the functions necessary to plot the P/L curve at expiration and its histogram from the historical data.
*  **Options.py** contains the definitions of the "Options" class and the computational part of the code.

## Main libraries used

*  pandas
*  matplotlib
*  statistics

---

## Documentation
Documentation is not available yet, but running the driver code is pretty straightforard. The example provided is for IEF (using real data from 01/28/2022) and below you can see the output:

Max profit: 78.0 at 112.5.<br/>
Max loss: -22.0 beyond 113.5 or 111.5.<br/>
See fig.1 for more details.<br/>
Expected utiliy (assuming no slippage and transaction costs): 16.34.<br/>
See fig.2 for more details.

![alt text](https://github.com/thanos713/Iron-butterfly-calculator/blob/main/pnl.png?raw=true)
![alt text](https://github.com/thanos713/Iron-butterfly-calculator/blob/main/histogram.png?raw=true)



## Credits
For this project, I claim credit both for the idea and the implementation; nobody else contributed.

