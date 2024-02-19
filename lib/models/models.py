from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class ModelAgency(Base):
    __tablename__ = 'model_agency'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    models = relationship('Model', back_populates='agency')