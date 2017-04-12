from sqlalchemy import create_engine,Table
from sqlalchemy.orm import sessionmaker
import sys
sys.path.append("..")
from conf import settings


engine = create_engine(settings.DB_CONN)
#engine = create_engine(settings.DB_CONN,echo=True)

SessionCls = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = SessionCls()