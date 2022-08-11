from sqlalchemy import Column,Integer,String,DateTime,Boolean,func,ForeignKey
from db.base_class import Base
from sqlalchemy.orm import relationship

class Todo(Base):
  __tablename__ = 'todos'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, unique=True , nullable=False)
  description = Column(String, nullable=False)
  completed = Column(Boolean, default=False)
  created = Column(DateTime(timezone=True),server_default=func.now())
  user_id = Column(String, ForeignKey('users.id'), nullable=False)
  user = relationship('User', back_populates='todos')


""" A one-to-many relationship between todo and user via the SQLAlchemy ForeignKey class."""
"""A bidirectional relationship where the “reverse” side is a many to one, we connect the tables using the relationship.back_populates parameter"""