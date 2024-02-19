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

def list_models_for_magazine():
    magazine_name = input("Enter the Magazine's name: ")
    models = get_models_for_magazine(magazine_name)

    if models:
        print(f"Models for {magazine_name}:")
        for model in models:
            print(f"Model ID: {model.id}, Name: {model.first_name} {model.last_name}")
    else:
        print(f"No models found for Magazine {magazine_name}")

def list_eligible_models():
    eligible_models = get_eligible_models()

    if eligible_models:
        print("Eligible Models for International Magazines:")
        for model in eligible_models:
            print(f"{model.first_name} {model.last_name} is eligible for international magazines.")
    else:
        print("No eligible models found for international magazines.")