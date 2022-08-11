from sqlalchemy import Column, Integer, String,Boolean
from db.base_class import Base
from sqlalchemy.orm import relationship

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True ,index=True)
  username = Column(String, unique=True, nullable= False)
  email = Column(String, nullable=False, unique= True)
  is_active = Column(Boolean, default=True)
  todos = relationship('Todo', back_populates='user',uselist=True)