import yfinance as yf

msft = yf.Ticker("DOGE-USD")
tesla = yf.Ticker("TSLA")

a =  msft.history(period="1d", interval="1m")
b = tesla.history(period="1d", interval= "1m")


a.to_csv('file1.csv')
b.to_csv('file2.csv')
