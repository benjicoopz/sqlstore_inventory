from sqlalchemy import create_engine, Column, Integer, String, Date
import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = sqlalchemy.orm.declarative_base()


class Product(Base):
    __tablename__ = 'inventory'

    product_id = Column(Integer, primary_key=True)
    product_name = Column('Product', String)
    product_quantity = Column('Amount', Integer)
    product_price = Column('Price', Integer)
    date_updated = Column('Date', Date)

    def __repr__(self):
        return (f'Product: {self.product_name} Amount: {self.product_quantity}'
                f' Price: {self.product_price} Date Updated: {self.date_updated}')