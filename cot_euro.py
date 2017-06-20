# Script to analyse the Commitment of Traders on the Euro/Dollar Future contract

import quandl
import pandas as pd
import matplotlib.pyplot as pl
import sys

# Import data from quandl.com
euro=quandl.get("CHRIS/CME_EC2")['Settle']   #euro price
cot=quandl.get("CFTC/EC_F_L_ALL")   #cot data
noncommercial_diff=cot['Noncommercial Long']-cot['Noncommercial Short']  #diff long/short noncommercial
commercial_diff=cot['Commercial Long']-cot['Commercial Short']  #diff long/short commercial

# Plot the data 
fig=pl.figure()
ax=fig.add_subplot(211)  #first subplot
ax.plot(euro, color ='b',label='Euro')  #plot euro price
pl.title('Non Commercial COT')
ax.legend(loc='center left')
ax2=ax.twinx()      #second axis for the cot data
ax2.plot(cot['Noncommercial Long'], color ='g',label='Long')
ax2.plot(cot['Noncommercial Short'], color ='r',label='Short')
pl.legend(loc='upper left')

aax=fig.add_subplot(212)  #second subplot
aax.plot(euro, color ='b',label='Euro')
aax.legend(loc='center left')
pl.title('Commercial COT')
aax2=aax.twinx()    #second axis for the cot data
aax2.plot(cot['Commercial Long'], color ='g',label='Long')
aax2.plot(cot['Commercial Short'], color ='r',label='Short')
pl.legend(loc='upper left')

pl.show()

# Merge data in a data frame
def save_csv():
    df=pd.concat([euro,euro,euro,euro, noncommercial_diff, commercial_diff], join='inner', axis=1)
    df.columns=['Settle', 'Settle', 'Settle', 'Settle', 'noncommercial','commercial']
    df.to_csv('C:\\Users\\Flavio Angeli\\Desktop\\files to VT\\cot_euro.csv',sep=' ')

# Ask if the user would like to save the data in csv format, otherwise exit
ask=input('Would you like to write data into put_call_spx.csv file (y) ? ')
if ask=='y':
    save_csv()
else:
    sys.exit(0)
