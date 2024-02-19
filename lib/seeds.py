from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, ModelAgency, Model, LocalMagazine

engine = create_engine('sqlite:///model_hub.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
