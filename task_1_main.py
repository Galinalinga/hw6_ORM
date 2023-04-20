import sqlalchemy
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from connection import Session, engine, session
from task_1_models import create_tables, Publisher, Book, Stock, Sale, Shop



def get_shops(publisher_name_id=None):
    
    items = session.query(
        Book.title, Shop.name, Sale.price, Sale.date_sale, 
    ).select_from(Shop).\
        join(Stock).\
        join(Book).\
        join(Publisher).\
        join(Sale).\
        filter(or_(
            Publisher.id == enter_values, Publisher.name == enter_values
        )).all()

    for Book.title, Shop.name, Sale.price, Sale.date_sale in items: 
        print(f"{Book.title: <40} | {Shop.name: <10} | {Sale.price: <8} | {Sale.date_sale.strftime('%d-%m-%Y')}") 
        


if __name__ == '__main__':
   
    enter_values = input("Введите имя или номер издателя: ")
    get_shops(publisher_name_id=enter_values)

session.close() 