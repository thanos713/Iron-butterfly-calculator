import matplotlib.pyplot as plt

def make_histogram(option, historical_pnl): 
    fig, ax = plt.subplots()
    ax.set_title("Expected P/L from historical data")
    ax.grid(b=None, which='both', axis='both', color='#2b2b2b', linewidth=0.3)
    plt.xlabel('P/L',fontsize=11)
    plt.ylabel('Percent', fontsize=11)
    plt.hist(historical_pnl, bins=int(100*option.spread/2.0), density=True, color = "skyblue", lw=0.2)
    
    
def make_pnl_plot(prices,vals):
    # Find where PNL changes from negative to positive to change color, from green to red
    pos1 = 0
    for i in range(0,len(vals)):
        if abs(vals[i]) < 1e-2 and pos1 == 0:
            pos1 = i
        elif abs(vals[i]) < 1e-2 and pos1 != 0:
            pos2 = i
    
    fig, ax = plt.subplots()
    ax.set_title("P/L curve")
    ax.grid(b=None, which='both', axis='both', color='#2b2b2b', linewidth=0.2)
    plt.xlabel('Strike price',fontsize=11)
    plt.ylabel('P/L', fontsize=11)
    plt.plot(prices[0:pos1+1], vals[0:pos1+1], color='red')
    plt.plot(prices[pos1:pos2+1], vals[pos1:pos2+1], color='green')
    plt.plot(prices[pos2:], vals[pos2:], color='red')
    ax.scatter(prices[pos1],vals[pos1], color='black')
    plt.text(prices[pos1], vals[pos1],str(round(prices[pos1],2)), verticalalignment='top')
    ax.scatter(prices[pos2],vals[pos2], color='black')
    plt.text(prices[pos2], vals[pos2],str(round(prices[pos2],2)), horizontalalignment='right', verticalalignment='top')


