import sqlalchemy
from sqlalchemy.orm import sessionmaker
from task_1_models import create_tables, Publisher, Book, Stock, Sale, Shop
from pprint import pprint

# создаем БД publishing_house 
DSN = 'postgresql://postgres:nehgjlrfa@localhost:5432/publishing_house'

engine = sqlalchemy.create_engine(DSN)   # объект для подключения к БД

Session = sessionmaker(bind=engine)  # Session-создатель сессий (класс)

session = Session()  # создаем экземпляр класса Session


# создание таблиц
create_tables(engine)
#
# заполнение таблицы издательств
publ_1 = Publisher(name='Азбука')
publ_2 = Publisher(name='АСТ')
publ_3 = Publisher(name='Эксмо')
publ_4 = Publisher(name='Иностранка')

session.add_all([publ_1, publ_2, publ_3, publ_4])
session.commit()

# заполнение таблицы магазинов
shop_1 = Shop(name='Буквоед')
shop_2 = Shop(name='Лабиринт')
shop_3 = Shop(name='Книжный дом')
shop_4 = Shop(name='Город книг')

session.add_all([shop_1, shop_2, shop_3, shop_4])
session.commit()

# заполнение таблицы книг
book_1 = Book(title='Война и мир', id_publisher=1)
book_2 = Book(title='Анна Каренина', id_publisher=1)
book_3 = Book(title='Тихий Дон', id_publisher=1)
book_4 = Book(title='Солярис', id_publisher=2)
book_5 = Book(title='Воришка Мартин', id_publisher=2)
book_6 = Book(title='Повелитель мух', id_publisher=2)
book_7 = Book(title='Охота на овец', id_publisher=3)
book_8 = Book(title='Убийство Командора', id_publisher=3)
book_9 = Book(title='1Q84', id_publisher=3)
book_10 = Book(title='Норвежский лес', id_publisher=3)
book_11 = Book(title='Маленький принц', id_publisher=4)
book_12 = Book(title='Планета людей', id_publisher=4)
session.add_all([book_1, book_2, book_3, book_4, book_5, book_6, book_7, book_8, book_9, book_10, 
                                                                               book_11, book_12])
session.commit()

# заполнение таблицы наличия товара
stock_1 = Stock(id_book=1, id_shop=1, count=2)
stock_2 = Stock(id_book=1, id_shop=2, count=1)
stock_3 = Stock(id_book=2, id_shop=3, count=2)
stock_4 = Stock(id_book=2, id_shop=4, count=2)
stock_5 = Stock(id_book=3, id_shop=1, count=1)
stock_6 = Stock(id_book=4, id_shop=2, count=3)
stock_7 = Stock(id_book=5, id_shop=4, count=1)
stock_8 = Stock(id_book=6, id_shop=1, count=4)
stock_9 = Stock(id_book=7, id_shop=1, count=5)
stock_10 = Stock(id_book=8, id_shop=2, count=3)
stock_11 = Stock(id_book=8, id_shop=3, count=1)
stock_12 = Stock(id_book=9, id_shop=2, count=3)
stock_13 = Stock(id_book=9, id_shop=3, count=4)
stock_14 = Stock(id_book=10, id_shop=4, count=5)
stock_15 = Stock(id_book=11, id_shop=3, count=1)
stock_16 = Stock(id_book=11, id_shop=1, count=2)
stock_17 = Stock(id_book=12, id_shop=3, count=3)


session.add_all([stock_1, stock_2, stock_3, stock_4, stock_5, stock_6, stock_7, stock_8, stock_9, stock_10,
                 stock_11, stock_12, stock_13, stock_14, stock_15, stock_16, stock_17])

session.commit()

# заполнение таблицы продаж
sale_1 = Sale(price=450, date_sale='01-03-2023', id_stock=1, count=1)
sale_2 = Sale(price=450, date_sale='02-03-2023', id_stock=2, count=1)
sale_3 = Sale(price=300, date_sale='01-03-2023', id_stock=3, count=2)
sale_4 = Sale(price=300, date_sale='02-03-2023', id_stock=4, count=2)
sale_5 = Sale(price=350, date_sale='02-03-2023', id_stock=5, count=1)
sale_6 = Sale(price=250, date_sale='02-03-2023', id_stock=6, count=1)
sale_7 = Sale(price=180, date_sale='03-03-2023', id_stock=7, count=1)
sale_8 = Sale(price=295, date_sale='04-03-2023', id_stock=8, count=1)
sale_9 = Sale(price=300, date_sale='07-03-2023', id_stock=9, count=3)
sale_10 = Sale(price=650, date_sale='07-03-2023', id_stock=10, count=2)
sale_11 = Sale(price=800, date_sale='07-03-2023', id_stock=13, count=1)
sale_12 = Sale(price=280, date_sale='04-04-2023', id_stock=14, count=2)
sale_13 = Sale(price=350, date_sale='10-04-2023', id_stock=15, count=1)
sale_14 = Sale(price=210, date_sale='08-04-2023', id_stock=17, count=1)
sale_15 = Sale(price=210, date_sale='10-04-2023', id_stock=17, count=2)

session.add_all([sale_1, sale_2, sale_3, sale_4, sale_5, sale_6, sale_7, sale_8, sale_9, sale_10, sale_11,
                 sale_12, sale_13, sale_14, sale_15])
session.commit()


#  Функция для построчного вывода фактов покупки книг конкретного издательства:

input_name = input('Введите название издательства: ')
input_id = input('Введите идентификатор издательства: ')

def get_shop_by_publisher(publisher_name=None, publisher_id=None):

    sudq = session.query(Shop.name, Stock.id).select_from(Shop).join(Stock).join(Sale).subquery()

    if publisher_id is not None and publisher_name is None:
        for q in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Sale). \
            join(Stock).join(Book).join(Shop).join(Publisher).join(sudq, Sale.id_stock == Stock.id).filter(Publisher.id
                                                                                            == int(publisher_id)):
            print(q)
    elif publisher_name is not None and publisher_id is None:
        for q in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Sale). \
            join(Stock).join(Book).join(Shop).join(Publisher).join(sudq, Sale.id_stock == Stock.id).filter(Publisher.name
                                                                                                == publisher_name):
            print(q)
    elif publisher_name is not None and publisher_id is not None:
        for q in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Sale). \
                join(Stock).join(Book).join(Shop).join(Publisher).join(sudq, Sale.id_stock == Stock.id).filter(Publisher.name
                                                                == publisher_name, Publisher.id == int(publisher_id)):
            print(q)


# ВЫЗОВ ФУНЦИИ 
# Если введено только название:
if __name__ == '__main__':
    get_shop_by_publisher(publisher_name=input_name)


# Если введен только идентификатор:
if __name__ == '__main__':
   get_shop_by_publisher(publisher_id=input_id)


# Если введены название и идентификатор:
if __name__ == '__main__':
    get_shop_by_publisher(publisher_id=input_id, publisher_name=input_name)


session.close() # закрытие сессии
