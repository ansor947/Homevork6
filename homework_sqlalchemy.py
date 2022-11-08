# Задание 2

import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import requests
import json
from pprint import pprint

login = 'postgres'
password = '230611End' 
db = 'Tips'

DSN = "postgresql://login:password@localhost:5432/db"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def show_publisher():
    name_publisher = input('Введите имя или id: ')
    for publisher in session.query(Publisher).filter(Publisher.name == name_publisher or Publisher.id == name_publisher).all():
        return publisher

# Задание 1

class Publisher(Base):
    __tablename__ = "publisher"
    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length = 60), unique = True)
    

class Book(Base):
    __tablename__ = "book"
    id = sq.Column(sq.Integer, primary_key = True) 
    title = sq.Column(sq.String(length = 60), unique = True) # уместно ли здесь unique, ведь назания книг могут совпадать у разных авторов? # Или определяющим будет лишь id(primary key)?                                                              
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable = False)
    publisher = relationship(Publisher, backref="book")

class Shop(Base):
    __tablename__ = "shop"
    id = sq.Column(sq.Integer, primary_key = True) 
    name = sq.Column(sq.String(length = 60), unique = True)  

class Stock(Base):
    __tablename__ = "stock"
    id = sq.Column(sq.Integer, primary_key = True) 
    count = sq.Column(sq.String(length = 60), unique = True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable = False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable = False)
    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

class Sale(Base):
    __tablename__ = "sale"
    id = sq.Column(sq.Integer, primary_key = True) 
    price = sq.Column(sq.String(length = 60), unique = True)
    count = sq.Column(sq.String(length = 60), unique = True)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable = False)
    stock = relationship(Stock, backref="sale")


create_tables(engine)

# Задание 3

def receive_data():
    with open(r'C:\Users\Андрей-сан\Desktop\py-homeworks-db\orm\fixtures\tests_data.json', 'rt', encoding='utf-8') as f:
        data = json.load(f)
        return data

def receive_fields(base_data):
    update_list = []
    for key in receive_data():
        if 'publisher' in key.values():
            instance_publisher = Publisher(id = key['pk'], name = key['fields']['name'] )
            update_list.append(instance_publisher)
    

        elif 'book' in key.values():
            update_list = []
            instance_book = Book(id = key['pk'], title = key['fields']['title'], publisher_id = key['fields']['publisher'])
            update_list.append(instance_book)

        elif 'shop' in key.values():
            update_list = []
            instance_shop = Shop(id = key['pk'], name = key['fields']['name'])
            update_list.append(instance_shop)

        elif 'stock' in key.values():
            update_list = []
            instance_stock = Stock(id = key['pk'], count = key['fields']['count'], book_id = key['fields']['book'], shop_id = key['fields']['shop'])
            update_list.append(instance_stock)

        elif 'sale' in key.values():
            update_list = []
            instance_sale = Sale(id = key['pk'], price = key['fields']['price'], count = key['fields']['count'], date_sale = key['fields']['date_sale'], shop_id = key['fields']['stock'])  
            update_list.append(instance_sale)

    return session.add_all(update_list), session.commit()

   
pprint(receive_fields(receive_data()))

session.close()
