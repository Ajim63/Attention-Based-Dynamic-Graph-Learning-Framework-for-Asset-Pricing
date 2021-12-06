

import numpy as np
import pandas as pd
import datetime
#import matplotlib.pyplot as plt
import networkx as nx
import copy
from datetime import datetime
import random


"""
### Variable Descriptions: 
prccd -- pric- close- daily
prchd -- price- high -daily 
prcld -- price -low- daily
prcod -- price-open-daily
eps -- current eps
cshtrd -- trading volume -daily
cshoc --shares outstanding
capgn -- capital gains
"""

#read the data



crsp = pd.read_csv('data/SP_daily.csv', parse_dates=['datadate'])
crsp.drop(['iid', 'gvkey', 'tic'], axis = 1, inplace = True)

#fill missing value
crsp['capgn'].fillna(0, inplace = True)
crsp['divd'].fillna(0, inplace = True)

#calculate return 
crsp["ret"] = crsp.groupby("cusip")['prccd'].apply(lambda x: np.log(x) - np.log(x.shift()))

#calculate all other necessary variables
crsp['size'] = np.log(crsp['cshoc']*crsp['prccd'])
crsp["log_vol"] = np.log(crsp['cshtrd'])
crsp["grvol"] = crsp.groupby("cusip")['cshtrd'].apply(lambda x: np.log(x) - np.log(x.shift()))
crsp["grshrout"] = crsp.groupby("cusip")['cshoc'].apply(lambda x: np.log(x) - np.log(x.shift()))

crsp['Trunover'] =  crsp['cshtrd']/crsp['cshoc']


crsp["log_prccd"] = np.log(crsp['prccd'])
crsp["log_prchd"] = np.log(crsp['prchd'])
crsp["log_prcld"] = np.log(crsp['prcld'])
crsp["log_prcod"] = np.log(crsp['prcod'])

crsp["m_w"] = crsp.groupby("cusip")['prccd'].apply(lambda x: np.log(x) - np.log(x.shift(5)))
crsp["m_2w"] = crsp.groupby("cusip")['prccd'].apply(lambda x: np.log(x) - np.log(x.shift(10)))
crsp["m_m"] = crsp.groupby("cusip")['prccd'].apply(lambda x: np.log(x) - np.log(x.shift(21)))
crsp["m_2m"] = crsp.groupby("cusip")['prccd'].apply(lambda x: np.log(x) - np.log(x.shift(42)))
crsp["m_3m"] = crsp.groupby("cusip")['prccd'].apply(lambda x: np.log(x) - np.log(x.shift(63)))
crsp["m_6m"] = crsp.groupby("cusip")['prccd'].apply(lambda x: np.log(x) - np.log(x.shift(126)))


#Calculate Variance
#crsp['var'] = crsp.groupby(['PERMNO'])['ret'].rolling(12).var().reset_index(0,drop=True)
crsp['Max_y'] = crsp.groupby(['cusip'])['prccd'].rolling(252).max().reset_index(0,drop=True)
crsp['Min_y'] = crsp.groupby(['cusip'])['prccd'].rolling(252).min().reset_index(0,drop=True)

crsp['Rel2High'] = (crsp['prccd']-crsp['Max_y'])/crsp['Max_y']
crsp['Rel2low'] = (crsp['prccd']-crsp['Min_y'])/crsp['Min_y']

crsp['spread'] = crsp["prchd"]-crsp["prcld"]
crsp['sp_opclose'] = crsp["prccd"]-crsp["prcod"]




#keep the data from Jan01,2011-Dec31,2020
crsp = crsp[crsp['datadate'] > '2010-12-31']

#keep only the required variables
crsp = crsp[['datadate', 'cusip', 'capgn', 'divd', 'eps', 'ret', 'size', 'log_vol', 'grvol',
       'grshrout', 'Trunover', 'log_prccd', 'log_prchd', 'log_prcld',
       'log_prcod', 'm_w', 'm_2w', 'm_m', 'm_2m', 'm_3m', 'm_6m', 'Max_y',
       'Min_y', 'Rel2High', 'Rel2low', 'spread', 'sp_opclose' ]]

#drop missing values
crsp.dropna(axis=0, how='any', inplace = True)



#Remove days that have very few stocks are traded
miss_days = crsp.groupby('datadate').size().to_frame()
miss_days = miss_days[miss_days[0]>300]
crsp = crsp[crsp["datadate"].isin(miss_days.index)]

n_days= len(crsp.groupby('datadate').size())
print(n_days)


constant_firm = crsp.groupby('cusip').size()
constant_firm = constant_firm[constant_firm == n_days]

crsp = crsp[crsp["cusip"].isin(constant_firm.index)]


## Save the clean file in a pickle dictrionary. 
crsp.to_pickle("daily_clear_ret.pickle")