import sqlalchemy
from sqlalchemy.orm import sessionmaker
from task_1_models import create_tables, Publisher, Book, Stock, Sale, Shop
from connection import Session, engine, session

class Filling:
    def __init__(self, session):
        self.session = session

    def create_publisher (self, name):
        publisher = Publisher(name=name)
        session.add(publisher)
        session.commit()
        return publisher

    def create_shop (self, name):
        shop = Shop(name=name)
        session.add(shop)
        session.commit()
        return shop

    def create_book(self, title, publisher):
        book = Book(title=title, id_publisher=publisher.id)
        session.add(book)
        session.commit()
        return book

    def create_sale(self, price, date_sale, stock, count):
        sale = Sale(price=price, date_sale=date_sale, id_stock=stock.id, count=count)
        session.add(sale)
        session.commit()
        return sale

    def create_stock(self, book, shop, count):
        stock = Stock(id_book=book.id, id_shop=shop.id, count=count)
        session.add(stock)
        session.commit()
        return stock