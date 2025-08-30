from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True,index = True)
    email = Column(String, nullable=False, unique=True, index=True)
    age = Column(Integer, nullable=True, index=True)
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id  =Column(Integer,ForeignKey("users.id"),index = True )
    user = relationship("User", back_populates = "orders")
