import pandas
import datetime
import pytz
import os
import time
import mysql.connector as mysql
import matplotlib.pyplot as plt
import numpy as np
import config
import psycopg2
from sqlalchemy import create_engine


def get_curr_date():
    my_timestamp = datetime.datetime.now()

    old_timezone = pytz.timezone("EET")
    new_timezone = pytz.timezone("US/Eastern")

    localized_timestamp = old_timezone.localize(my_timestamp)
    new_timezone_timestamp = localized_timestamp.astimezone(new_timezone)

    return new_timezone_timestamp.strftime("%Y, %-m, %-d, %-H, %-M")


def convert_to_dataframe(data: list):
    df = pandas.DataFrame(data)
    df.transpose()

    df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'dividends', 'stocksplits']
    return df



def calculate_rsi(dataframe, window_length=14):
    close = dataframe['close']
    delta = close.diff()
    # Get rid of the first row, which is NaN
    delta = delta[1:]
    #print(delta)
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
#     # Calculate the EWMA
#     roll_up1 = up.ewm(span=window_length).mean()
#     roll_down1 = down.abs().ewm(span=window_length).mean()
#     # Calculate the RSI based on EWMA
#     RS1 = roll_up1 / roll_down1
#     RSI1 = 100.0 - (100.0 / (1.0 + RS1))


    # Calculate the SMA
    roll_up2 = up.rolling(window_length).mean()
    roll_down2 = down.abs().rolling(window_length).mean()
    # Calculate the RSI based on SMA
    RS2 = roll_up2 / roll_down2
    RSI2 = 100.0 - (100.0 / (1.0 + RS2))

    return RSI2



def add_two_moving_averages(df, first_period: int, second_period: int, moving_average_template: str):
    if first_period > 0 and second_period > 0:
        df[moving_average_template+str(first_period)] = df['close'].rolling(window=first_period).mean()
        df[moving_average_template+str(second_period)] = df['close'].rolling(window=second_period).mean()
    else:
        print("Periods for moving averages have to be more than 0")

def add_two_exponential_moving_averages(df, first_period: int, second_period: int, moving_average_template: str):
    if first_period > 0 and second_period > 0:
        df[moving_average_template+str(first_period)] = df['close'].ewm(span = first_period, adjust = False).mean()
        df[moving_average_template+str(second_period)] = df['close'].ewm(span = second_period, adjust = False).mean()
    else:
        print("Periods for moving averages have to be more than 0")

def get_database_data():

    engine_str = 'postgresql://' + config.db_usr + ':' + config.db_pass + '@localhost/borader'
    engine = create_engine(engine_str)

    with engine.begin() as cn:
        sql = """SELECT * from myfinaltable"""
        data = cn.execute(sql).fetchall()
    return data


# Transforming data(list) to dataframe
# Dataframe has more options for making trading strategies
df = convert_to_dataframe(get_database_data())

def make_buy_sell_strategy(df, strategy_label_one, strategy_label_two):
    #TODO Exeption if strategy_labels aren't matching

    df['signal'] = 0.0
    df['signal'] = np.where(df[strategy_label_one] > df[strategy_label_two], 1.0, 0.0)

    # Get the difference between element-to element
    # That way you can track when xMA is crossing yMA
    # When xMA pass over yMA - buy
    # When xMA pass under yMA - sell
    df['position'] = df['signal'].diff()

def print_results_from_strategy(start_index: int):
    # This is dumb but for now works
    df = convert_to_dataframe(get_database_data())
    is_stock_bought = False
    price_bought = 0
    is_stock_sold = False
    price_sold = 0
    won = 0
    close_price = 0
    money = 1000
    print(f"Starting with {money}.")
    for i in range(start_index, len(df)):
        close_price = df.loc[i]['close']
        if df.loc[i]['position'] == 1:
            if is_stock_sold:
                print(f"Closed position at price level: {close_price}! Price range: {price_sold - close_price}")
                money -= int(close_price * 1.01)
                won += price_sold - close_price
                is_stock_sold = False
            print(f"Bought Tesla possition when price level: {close_price}")
            money -= int(close_price * 1.01)
            price_bought = close_price
            is_stock_bought = True
            print(f"Current money {money}")
        elif df.loc[i]['position'] == -1:
            if is_stock_bought:
                print(f"Closed position at price level: {close_price}! Price range: {close_price - price_bought}")
                money += int(close_price)
                won += close_price - price_bought
                is_stock_bought = False
            print(f"Sold Tesla position when price level: {close_price}")
            money += int(close_price)
            is_stock_sold = True
            price_sold = close_price
            print(f"Current money {money}")

    if is_stock_sold:
        print(f"Closed position! Price range: {price_sold - close_price}")
        money -= int(close_price * 1.01)
        won += price_sold - close_price
        is_stock_sold = False

    if is_stock_bought:
        print(f"Closed position! Price range: {close_price - price_bought}")
        money += int(close_price)
        won += close_price - price_bought
        is_stock_bought = False

    print(f"End up with {money}!!!")

    return money


period_one = 60 # 30 for the win - EMA: 50 for the win
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

start_index = 4
# print(print_results_from_strategy(df, start_index))

#print(df)
"""for d in range(2, 9):
    ma_one = 'EMA'+str(period_one)
    df.drop(ma_one, axis=1, inplace=True)"""

def display():
    plt.figure(figsize=(10,10))
    plt.tick_params(axis = 'both', labelsize = 10)
    plt.plot(df.loc[start_index:]['close'], label="close")
    """plt.plot(df.loc[900:][ma_label_one], 'g--', label=ma_label_one)
    plt.plot(df.loc[900:][ma_label_two], 'r--', label=ma_label_two)"""

    # After visualizing ma and ema :
    # Results: EMA is more accurate and will potentially win more money
    plt.plot(df.loc[start_index:][ma_one], 'y--', label=ma_one)
    plt.plot(df.loc[start_index:][ma_two], 'b--', label=ma_two)

    # Plot buy signals
    plt.plot(df.loc[start_index:][df.loc[start_index:]['position'] == 1].index,
             df.loc[start_index:][ma_one][df.loc[start_index:]['position'] == 1],
             '.', markersize = 10, color = 'g', label = 'buy')
    # Plot sell signals
    plt.plot(df.loc[start_index:][df.loc[start_index:]['position'] == -1].index,
             df.loc[start_index:][ma_one][df.loc[start_index:]['position'] == -1],
             '.', markersize = 10, color = 'r', label = 'sell')

    plt.legend()
    plt.xlabel("date")
    plt.ylabel("$ price")
    plt.grid()
    #plt.show()
    if os.path.exists("web_ui/static/images/chart.png"):
        os.remove("web_ui/static/images/chart.png")
        print("removing chart png")
    else:
        print("The file does not exist")
    plt.savefig("web_ui/static/images/chart.png")
    #return 0
