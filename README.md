# Euro FX Commitment of Traders Analysis

## Commitment of Traders (COT)

The Commitment of traders is a weekly report issued by the [Commodity Futures Trading Commission (CFTC)](http://www.cftc.gov) containing the holdings of participants 
in various futures markets in the United States. The data collected by the CFTC covers positions in futures on financial instruments, metals, petroleum, currencies and other commodities.
The COT reports provide a breakdown of each Tuesday's open interest for markets in which 20 or more traders hold positions equal to or above the reporting levels established by the CFTC.
For example, some reports show data for commercial and non commercial holdings, spreading, changes from previous report, percents of open interest by category, and number of traders.

Before moving on, it is important a few terms as defined by the CFTC.

#### Open Interest 

Open Interest is the toal of all futures and/or option contracts entered into and not yet offset by a transaction, by delivery, by exercise, etc. The aggregate of all long open interest is equal to the aggregate of all short open interest.

#### Commercial and Non-commercial Traders

When an individual reportable trader is identified to the Commission, the trader is classified either as "commercial" or "non-commercial." All of a trader's reported futures positions in a commodity are classified as commercial if the trader uses futures contracts in that particular commodity for hedging as defined in CFTC Regulation 1.3, 17 CFR 1.3(z). A trading entity generally gets classified as a "commercial" trader by filing a statement with the Commission, on CFTC Form 40: Statement of Reporting Trader, that it is commercially "...engaged in business activities hedged by the use of the futures or option markets."


## The Script

The script, called *cot_euro.py*, downloads the data and plots the historical series of Euro and COT.

#### Data

The data used are downloaded using the Quandl's API. 

The Future contract on the Euro/Dollar exchange is the underlying instrument that the investors disclosed in the CFTC report are trading.
For this reason the script downloads the historical data for the [Euro FX](https://www.quandl.com/data/CHRIS/CME_EC2-Euro-FX-Futures-Continuous-Contract-2-EC2).
The database obtained shows different prices for the Euro FX contract (open, high, low, last, settle,...), but only *Settle* is used in the chart.

The [COT data](https://www.quandl.com/data/CFTC/EC_F_L_ALL-Commitment-of-Traders-Euro-Fx-Futures-Only-Legacy-Format-099741) database contains information 
regarding the open positions (long, short, spread) of different type of investors (non commercial, commercial, total, non reportable). 
The series considered in this case are *Commercial Long, Commercial Short, Non Commercial Long and Non Commercial Short*.

#### Chart analysis

After downloading the data, the script plots the following historical series:

* Euro FX
* Commercial Long
* Commercial Short
* Non Commercial Long
* Non Commercial Short

After plotting the data, the script also asks if the user would like to save the data as a csv file.

## Objective

The objective of this simple script is to analyse and monitor the open positions of commercial and non commercial traders. 
The comparison Short / Long positions shows which net position the market is taking. 
The hypothesis here is that the position taken by these investors can influence the price movement of the Euro FX.
If Non Commercial traders have for example a net long position, this means that most of them are buying contracts with the expectation of a price increase.
If Commercial traders have for example a net long position, this means that most of them are buying contracts to hedge their commercial activities against a price decrease. 