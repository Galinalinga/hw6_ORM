import sqlalchemy
from sqlalchemy.orm import sessionmaker

DSN = 'postgresql://postgres:nehgjlrfa@localhost:5432/publishing_house'
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()