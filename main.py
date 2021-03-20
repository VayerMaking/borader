import yfinance as yf
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Numeric, MetaData

engine = create_engine('mysql+pymysql://root:vayertues@localhost:3306/borader')

# Session = sessionmaker(bind=engine)
# session = Session()
#
# Base = declarative_base()


# class Product(Base):
#     __tablename__ = 'products'
#     id=Column(Integer, primary_key=True)
#     title=Column('title', String(32))
#     in_stock=Column('in_stock', Boolean)
#     quantity=Column('quantity', Integer)
#     price=Column('price', Numeric)
#
#     def __init__(self, title, in_stock, quantity, price):
#         self.title = title
#         self.in_stock = in_stock
#         self.quantity = quantity
#         self.price = price
#
# Product.__table__.create(bind=engine, checkfirst=True)


# class Stock_Data(Base):
#     __tablename__ = 'stock_data'
#     id=Column(Integer, primary_key=True)
#     datetime=Column('date', DateTime)
#     open=Column('open', Numeric)
#     high=Column('high', Numeric)
#     low=Column('low', Numeric)
#     close=Column('close', Numeric)
#     volume=Column('volume', Integer)
#
#     def __init__(self, datetime, open, high, close, low, volume):
#         self.datetime = datetime
#         self.high = high
#         self.open = open
#         self.low = low
#         self.close = close
#         self.volume = volume
#
# Stock_Data.__table__.create(bind=engine, checkfirst=True)

doge = yf.Ticker("DOGE-USD")
tesla = yf.Ticker("TSLA")

dh =  doge.history(period="1d", interval="1m")
# b = tesla.history(period="1d", interval= "1m")
#
#
# a.to_csv('file1.csv')
# b.to_csv('file2.csv')
#print(tesla.info)
th = tesla.history(period="1d", interval="1m")

# print(tesla_historical.to_string())
# print(tesla_historical["High"])
# print(th.index)
# for i in th.index:
#
#     #print(th.keys())
#      #print(tesla_historical['Open'][i], tesla_historical['High'][i])
#     #i  = str(i)
#     #i = datetime.strptime(i, '%y-%m-%d %H:%M:%S-%f')
#     print(i)
#     session.add(Stock_Data(i, th['Open'][i], th['High'][i], th['Low'][i], th['Close'][i], th['Volume'][i]))
#     session.commit()

th.to_sql('asdf', con=engine, if_exists='replace')

with engine.begin() as cn:
   sql = """INSERT INTO myFinalTable (Datetime, Open, High, Low, Close, Volume, Dividends)
            SELECT t.Datetime, t.Open, t.High, t.Low, t.Close, t.Volume, t.Dividends
            FROM asdf t
            WHERE NOT EXISTS
                (SELECT 1 FROM myFinalTable f
                 WHERE t.Datetime = f.Datetime)"""

   cn.execute(sql)

# asdf = Product("The Bourne Identity", True, 100, 99.99)
#
# session.add(asdf)

# 10 - commit and close session
# session.commit()
# session.close()
