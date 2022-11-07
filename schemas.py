from pydantic import BaseModel

class AddressBook(BaseModel):
    latitude:str
    longtitude:str
    address_name:str
    adress_line1:str
    adress_line2:str
    city:str
    state:str
    country:str
    pincode:int