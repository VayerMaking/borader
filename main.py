import yfinance as yf
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Numeric, MetaData, Table
from sqlalchemy.ext.automap import automap_base

Base = automap_base()

class myFinalTable(Base):
     __tablename__ = 'myFinalTable'

     datetime = Column('DateTime', DateTime, primary_key=True)
     open = Column('Open', Numeric)
     high = Column('High', Numeric)
     Low = Column('Low', Numeric)
     Close = Column('Close', Numeric)
     volume = Column('Volume', Integer)
     dividends = Column('Dividends', Integer)
     stock_splits = Column('Stock Splits', Integer)

engine = create_engine('mysql+pymysql://root:Asdf123er!@localhost:3306/borader')
class myFinalTable(Base):
    __table__ = Table('myFinalTable', Base.metadata,
                    autoload=True, autoload_with=engine)

#Asdf = Base.classes.asdf
#a = Base.classes.myFinalTable

session = Session(engine)
Base.prepare(engine, reflect=True)

res = session.query(myFinalTable).first()
#print(res.Volume)

doge = yf.Ticker("DOGE-USD")
tesla = yf.Ticker("TSLA")

dh =  doge.history(period="1d", interval="1m")

th = tesla.history(period="1mo", interval="5m")

th.to_sql('asdf', con=engine, if_exists='append')

with engine.begin() as cn:
   sql = """INSERT INTO myFinalTable (Datetime, Open, High, Low, Close, Volume, Dividends)
            SELECT t.Datetime, t.Open, t.High, t.Low, t.Close, t.Volume, t.Dividends
            FROM asdf t
            WHERE NOT EXISTS
                (SELECT 1 FROM myFinalTable f
                 WHERE t.Datetime = f.Datetime)"""

   cn.execute(sql)


