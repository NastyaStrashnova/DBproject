from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
import connection_to_db
from connection_to_db import engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Code(Base):

    __tablename__ = 'Code'

    code_id = Column(String(10), primary_key=True)
    name = Column(String(40))
    action = Column(Integer)
'''
    def __repr__(self):
        return '<Code %r' % self.code_id

'''


class Users(Base):

    __tablename__ = 'Users'

    email = Column(String(30), primary_key=True)
    code_id = Column(String(10))
    password = Column(String(30))
    UniqueConstraint(email)

'''
    def __repr__(self):
        return '<Users %r' %self.code_id
'''




class Books(Base):

    __tablename__ = 'books'


    id = Column(Integer, primary_key=True)
    title = Column(String(40))
    author = Column(String(50))
    year = Column(String(4))
    description = Column(String(200))
    count = Column(Integer)
'''
    def __repr__(self):
        return '<Books %r' %self.id
'''

class User_list(Base):

    __tablename__ = 'user_list'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(10))
    b_in_basket = Column(Integer)
    wish_list = Column(Integer)

class User_books(Base):

    __tablename__ = 'user_books'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(10))
    books = Column(Integer)
    placement = Column(String(40)) #home or library


Base.metadata.create_all(engine)


