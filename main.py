import yfinance as yf# stock data api
from datetime import datetime, timedelta
import time
from sqlalchemy import create_engine#
from sqlalchemy.ext.declarative import declarative_base#                            SQl
from sqlalchemy.orm import sessionmaker, Session#                                                 Alchemy
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Numeric, MetaData, Table#   libs
from sqlalchemy.ext.automap import automap_base
from multiprocessing import Process # for threading
import strategy #strategy.py
import strategy_2
from web_ui import web_server
import config # config module with usernames and passes
import os

Base = automap_base()


class myfinaltable(Base):
     __tablename__ = 'myfinaltable'

     datetime = Column('datetime', DateTime, primary_key=True)
     open = Column('open', Numeric)
     high = Column('high', Numeric)
     Low = Column('low', Numeric)
     Close = Column('close', Numeric)
     volume = Column('volume', Integer)
     dividends = Column('dividends', Integer)
     stock_splits = Column('stock_splits', Integer)

engine_str = 'postgresql://' + config.db_usr + ':' + config.db_pass + '@localhost/borader'
engine = create_engine(engine_str)

class myfinaltable(Base):
    __table__ = Table('myfinaltable', Base.metadata,
                    autoload=True, autoload_with=engine)

#session = Session(engine)
Base.prepare(engine, reflect=True)
#with Session(engine) as connection:
#    res = connection.query(myfinaltable).first()

#Asdf = Base.classes.asdf
#a = Base.classes.myfinaltable
#print(res.Volume)

def get_data_to_db():
    while True:
        doge = yf.Ticker("DOGE-USD")
        tesla = yf.Ticker("TSLA")

        dh =  doge.history(period="1d", interval="1m")
        #past_time = timedelta(hours = 1)
        today = datetime.now().date()
        yesterday = today - timedelta(1)
        print(today)
        print(yesterday)
        #th = tesla.history(start=today, end=today, interval="1m")
        th = tesla.history(start=yesterday, end=today, interval="1m")
        #th = tesla.history(period="1d", interval="1m")#, start=datetime.now().date())
        #th = tesla.history(start= datetime.now() - past_time, end=datetime.now(), interval="1m")
        th.reset_index(inplace=True)
        print(th.columns)
        th.rename(columns = {'Datetime' : 'datetime', 'Open' : 'open', 'High' : 'high', 'Low' : 'low', 'Close' : 'close', 'Volume' : 'volume', 'Dividends' : 'dividends'}, inplace = True)
        print(th)
        th.to_sql('asdf', con=engine, if_exists='append')

        with engine.begin() as cn:
            sql = """INSERT INTO myfinaltable (datetime, open, high, low, close, volume, dividends)
                    SELECT t.Datetime, t.Open, t.High, t.Low, t.Close, t.Volume, t.Dividends
                    FROM asdf t
                    WHERE NOT EXISTS
                        (SELECT 1 FROM myfinaltable f
                        WHERE t.Datetime = f.Datetime)"""

            cn.execute(sql)

        print("completed a full cycle")
        time.sleep(10)

def analyze_data():
    while True:
        strategy_2.print_results_from_strategy(10)
        strategy_2.display()

def start_server():
    web_server.server_run()
    #os.system('python web_ui/web_server.py')


if __name__=='__main__':
    p1 = Process(target = get_data_to_db)
    p1.start()
    p2 = Process(target = analyze_data)
    p2.start()
    p3 = Process(target = start_server)
    p3.start()
    #print(web_server.web_ui_settings)
