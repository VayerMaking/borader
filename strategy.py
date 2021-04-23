"""
Plan:
	-Set strategy
	-Backtest that strategy using old datqa from API
	-Analizing the backtested results
	-If the analise is ok(50%+) than usse the strategy

Current API we are using - yahoo api
Brokers:
	-Etoro (no API)
	-Webull (github API)
	-Robinhood
Basic strategies:
  -5MA crossing 20MA
  -Volume
  -Trends
  -News

  Buying and selling stock:
  	-Selling stock at 1-2% win and (???) loss
  	-Stock should be (10-15)% of user portfolio

cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print(databases)

First strategy that I am gona use is 20MA crossing 5MA. This strategy is the simplest one
For strategy you should use this: https://github.com/CryptoSignal/Crypto-Signal"""




