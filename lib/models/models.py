from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class ModelAgency(Base):
    __tablename__ = 'model_agency'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    models = relationship('Model', back_populates='agency')
    
class Model(Base):
    __tablename__ = 'model'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    agency_id = Column(Integer, ForeignKey('model_agency.id'))
    agency = relationship('ModelAgency', back_populates='models')
    local_magazine = relationship('LocalMagazine', back_populates='model', uselist=False)
    photo_shoots = Column(Integer)
    
class LocalMagazine(Base):
    __tablename__ = 'local_magazine'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model_id = Column(Integer, ForeignKey('model.id'))
    model = relationship('Model', back_populates='local_magazine')

 