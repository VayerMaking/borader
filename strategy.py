'''
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

'''

"""minutes = 240

def get_curr_date():
	my_timestamp = datetime.datetime.now()

	old_timezone = pytz.timezone("EET")
	new_timezone = pytz.timezone("US/Eastern")

	localized_timestamp = old_timezone.localize(my_timestamp)
	new_timezone_timestamp = localized_timestamp.astimezone(new_timezone)

	l = list(new_timezone_timestamp.strftime("%z"))
	l.insert(3, ":")
	return new_timezone_timestamp.strftime("%Y-%m-%d %H:%M") + ":00" + ''.join(l)

#curr_time = get_curr_date()
#print(curr_time)
#time.sleep(20)

os.system('python main.py')

df = pandas.read_csv('file2.csv')

with open("file2.csv", 'r') as fd:
	list_data = []
	for line in fd:
		l = list(line.split(","))
		list_data.append(l)


# Get data from database


price_moved = 0;

day_high_price = float(list_data[1][4])
day_low_price = float(list_data[1][4])

for i in range(2, len(list_data), 1):
	price_before_minute = float(list_data[i - 1][4])
	curr_price = float(list_data[i][4])
	if curr_price > day_high_price:
		day_high_price = curr_price
	if curr_price < day_high_price:
		day_low_price = curr_price
	difference = price_before_minute - curr_price
	if difference <= 0:
		print(f"Down: {difference}")
	else:
		print(f"Up: {difference}")

	price_moved += difference

print(price_moved)
print(day_high_price)
print(day_low_price)
print(len(list_data))"""

import pandas
import datetime
import pytz
import os
import time
import mysql.connector as mysql
import matplotlib.pyplot as plt

def get_curr_date():
	my_timestamp = datetime.datetime.now()

	old_timezone = pytz.timezone("EET")
	new_timezone = pytz.timezone("US/Eastern")

	localized_timestamp = old_timezone.localize(my_timestamp)
	new_timezone_timestamp = localized_timestamp.astimezone(new_timezone)

	return new_timezone_timestamp.strftime("%Y, %-m, %-d, %-H, %-M")


"""def convert_to_dataframe(data: list):
	dataframe = pandas.DataFrame(data)
	dataframe.transpose()

	dataframe.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
	dataframe['datetime'] = dataframe.timestamp.apply(
	    lambda x: pandas.to_datetime(datetime.fromtimestamp(x / 1000).strftime('%c'))
	)

	dataframe.set_index('datetime', inplace=True, drop=True)
	dataframe.drop('timestamp', axis=1, inplace=True)
	return dataframe

print(get_curr_date())

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Asdf123er!",
    database = "borader"
)

cursor = db.cursor()

query = "SELECT * from myFinalTable"

cursor.execute(query)
data = cursor.fetchall()
close_price = []
for d in data:
	close_price.append(d[4])

#print(convert_to_dataframe(data))
print(type(data[0]))

plt.plot(close_price)
plt.show()"""

def get_x_ticks(date):
	prev_date = datetime.datetime(2021, 3, 24, 15, 49)
	#loop through df and then find index of prev date
	# sum_time = prev_date.index - date.index
	# i need 5 portions 
	#sum_time / 2 = tick
	# for i in range(5):
	# result.append(df.loc[prev_date.index + tick * i] ['timestamp'])
	# - | - | - | - | -

"""
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print(databases)"""


"""
First strategy that I am gona use is 20MA crossing 5MA. This strategy is the simplest one
For strategy you should use this: https://github.com/CryptoSignal/Crypto-Signal
"""





