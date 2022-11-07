from fastapi import FastAPI, Body, Depends, status, HTTPException
import schemas
from models import AddressBook

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()


@app.get("/")
def getAddress(session: Session = Depends(get_session)):
    addesses = session.query(AddressBook).all()
    return addesses

@app.get("/{id}")
def getAddress(id:int, session: Session = Depends(get_session)):
    addess = session.query(AddressBook).get(id)
    return addess


@app.post("/")
def addAddress(addess:schemas.AddressBook, session: Session = Depends(get_session), status_code=status.HTTP_201_CREATED):
    addess = AddressBook(latitude = addess.latitude,
    longtitude=addess.longtitude,
    address_name = addess.address_name,
    adress_line1 = addess.adress_line1,
    adress_line2 = addess.adress_line2,
    city = addess.city,
    state = addess.state,
    country = addess.country,
    pincode = addess.pincode)
    session.add(addess)
    session.commit()
    session.refresh(addess)

    return addess


@app.put("/{id}")
def updateAddress(id:int, addess:schemas.AddressBook, session: Session = Depends(get_session)):
    addessObject = session.query(AddressBook).get(id)
    addessObject.latitude = addess.latitude
    addessObject.longtitude = addess.longtitude
    addessObject.address_name = addess.address_name,
    addessObject.adress_line1 = addess.adress_line1,
    addessObject.adress_line2 = addess.adress_line2,
    addessObject.city = addess.city,
    addessObject.state = addess.state,
    addessObject.country = addess.country,
    addessObject.pincode = addess.pincode
    session.commit()
    return addessObject

@app.delete("/{id}")
def deleteAddress(id:int, session: Session = Depends(get_session)):
    addessObject = session.query(AddressBook).get(id)
    session.delete(addessObject)
    session.commit()
    session.close()
    return 'Addess was deleted...'