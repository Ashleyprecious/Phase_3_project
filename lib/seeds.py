from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, ModelAgency, Model, LocalMagazine

engine = create_engine('sqlite:///model_hub.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def seed_data():

    if session.query(ModelAgency).count() > 0:
        print("Seed data already exists. Skipping.")
        return
    
    
    agency1 = ModelAgency(name='Elite Models')
    agency2 = ModelAgency(name='Top Models')
    agency3 = ModelAgency(name='Global Talents')
    session.add_all([agency1, agency2,agency3])
    session.commit()



