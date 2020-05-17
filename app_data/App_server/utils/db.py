import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
basedir = os.path.abspath((os.path.dirname(os.path.dirname(__file__))))
sqlalchemy_db_uri = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
engine = create_engine(sqlalchemy_db_uri)
session = scoped_session(sessionmaker(bind=engine))
