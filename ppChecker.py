import os
from os.path import isfile, join
import pandas as pd

number = 365
mypath = os.getcwd()
onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]

for i in onlyfiles:
    if i.endswith('.prn'):
        file = pd.read_csv(i)

        if len(file) > number:
            close = file['<CLOSE>'][len(file)-1]
            high = max(file['<HIGH>'][-number:])
            low = min(file['<LOW>'][-number:])
            try:
                pp = ((2*close)+high+low)/4
                SMA200 = pd.Series.ewm(file['<CLOSE>'], span=200).mean()
                if close > pp and SMA200[len(file)-1] < close:
                    print(i.split('.')[0])
            except:
                print("Can not do the math!")
