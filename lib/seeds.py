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

    model1 = Model(first_name='Joy', last_name='Vheey', agency=agency1, local_magazine=None, photo_shoots=15)
    model2 = Model(first_name='Jane', last_name='Smith', agency=agency2, local_magazine=None, photo_shoots=5)
    model3 = Model(first_name='John', last_name='Makani', agency=agency3, local_magazine=None, photo_shoots=7)
    model4 = Model(first_name='Precious', last_name='Yelsha', agency=agency2, local_magazine=None, photo_shoots=17)
    model5 = Model(first_name='David', last_name='Charo', agency=agency1, local_magazine=None, photo_shoots=3)
    model6 = Model(first_name='Emily', last_name='Clark', agency=agency3, local_magazine=None, photo_shoots=9)
    session.add_all([model1, model2, model3, model4, model5, model6])
    session.commit()

    magazine1 = LocalMagazine(name='Fashion Weekly', model=model1)
    magazine2 = LocalMagazine(name='Glamour Magazine', model=model2)
    magazine3 = LocalMagazine(name='Style Magazine', model=model3)
    session.add_all([magazine1, magazine2,magazine3])
    session.commit()

if _name_ == '_main_':
    seed_data()