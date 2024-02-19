from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, ModelAgency, Model, LocalMagazine

engine = create_engine('sqlite:///model_hub.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

def list_models_under_agency():
    agency_name = input("Enter the Model Agency's name: ")
    models = get_models_under_agency(agency_name)

    if models:
        print(f"Models under {agency_name}:")
        for model in models:
            print(f"Model ID: {model.id}, Name: {model.first_name} {model.last_name}")
    else:
        print(f"No models found for Model Agency {agency_name}")