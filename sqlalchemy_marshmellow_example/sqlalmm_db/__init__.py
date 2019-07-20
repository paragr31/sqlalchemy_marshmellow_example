import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = sa.create_engine('sqlite:///example_sqlmm.db', echo=False)
Session = orm.scoped_session(orm.sessionmaker())
Session.configure(bind=engine)

