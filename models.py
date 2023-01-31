from sqlalchemy import Column, Integer, String
from database import Base

class Countries(Base):
    __tablename__ = "countries"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    

# https://www.youtube.com/watch?v=34jQRPssM5Q here we have the explanation