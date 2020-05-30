from my_functions import create_account, log_in, search_by_criteria, show_favourites, show_basket, put_in_favourites, count_of_books, delete_after_24_hours, put_in_basket, delete_from_favourites,place_the_order, recieve_book, back_to_library
from connection_to_db import engine
from db import Users, Code, Books, User_books, Base, User_list
from sqlalchemy.sql import select, update, join
from sqlalchemy import and_, or_, between, asc, desc,update
from sqlalchemy.orm import sessionmaker
import time

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


create_account('NM56777755','john', 'password44')

session.commit()