
from pandas_datareader import DataReader

import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np



###############################################################################
# Retrieve the data from Internet

# Choose a time period
d1 = datetime.datetime(2001, 01, 01)
d2 = datetime.datetime(2012, 01, 01)

#get the tickers
price = DataReader("MMM", "yahoo",d1,d2)['Adj Close']
price = price.asfreq('B').fillna(method='pad')

ret = price.pct_change()

#choose the quantile
quantile=0.05
#the vol window
volwindow=50
#and the Var window for rolling
varwindow=250

###############################################################################

#simple VaR using all the data
unnormedquantile=pd.expanding_quantile(ret,quantile)

#similar one using a rolling window
unnormedquantileR=pd.rolling_quantile(ret,varwindow,quantile)

#we can also normalize the returns by the vol
vol=pd.rolling_std(ret,volwindow)*np.sqrt(256)
unitvol=ret/vol

#and get the expanding or rolling quantiles
Var=pd.expanding_quantile(unitvol,quantile)
VarR=pd.rolling_quantile(unitvol,varwindow,quantile)

normedquantile=Var*vol
normedquantileR=VarR*vol
