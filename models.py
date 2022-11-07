from sqlalchemy import Column, Integer, String
from database import Base 

class AddressBook(Base):
    __tablename__ = 'addressbook'
    id = Column(Integer, primary_key=True)
    latitude = Column(String(256))
    longtitude = Column(String(256))
    address_name = Column(String(256))
    adress_line1 = Column(String(256))
    adress_line2 = Column(String(256))
    city = Column(String(256))
    state= Column(String(256))
    country = Column(String(256))
    pincode = Column(Integer())