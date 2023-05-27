from datetime import date, timedelta
from os import name
from flask import *
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData
metadata = MetaData()

howdate = Flask(__name__)
howdate.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
howdate.config['SQLALCHEMY_BINDS'] = {
    'sub1':      'sqlite:///sub1.db',
    'sub2':      'sqlite:///sub2.db',
    'sub3':      'sqlite:///sub3.db',
    'sub4':      'sqlite:///sub4.db',
    'sub5':      'sqlite:///sub5.db'

}
db = SQLAlchemy(howdate)



start_date = date(2019, 1, 1)
end_date = date(2020, 1, 1)
delta = timedelta(days=1)
dlist=[]
while start_date <= end_date:
    value = str(start_date.strftime("%m/%d/%Y"))
    # print(value.replace("-", "/"))
    dlist.append(value)
    start_date += delta

# print(dlist)


hello =  [Column(str(i), String,) for i in dlist]
sub2 = Table('sub2', metadata, *hello)
print (sub2.__dict__)
print (sub2.__dict__.get("_columns"))
