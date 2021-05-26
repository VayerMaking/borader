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

import thread


period_one = 50 # 30 for the win - EMA: 50 for the win 
period_two = 200 # 60 for the win - EMA: 200 for the win
"""moving_average_template = "SMA"
add_two_moving_averages(df, period_one, period_two, moving_average_template)

ma_one = moving_average_template+str(period_one)
ma_two = moving_average_template+str(period_two)

get_buy_sell_decision(df, ma_one, ma_two)"""

moving_average_template = "EMA"
add_two_exponential_moving_averages(df, period_one, period_two, moving_average_template)
ma_one = moving_average_template+str(period_one)
ma_two = moving_average_template+str(period_two)

make_buy_sell_strategy(df, ma_one, ma_two)
df1 = calculate_rsi(df)
res = []
for d in df1:
    res.append(d)

df['rsi'] = convert_to_dataframe(res, columns=['rsi'])
start_index = 50
res = print_results_from_strategy(df, start_index, "Tesla")

try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
