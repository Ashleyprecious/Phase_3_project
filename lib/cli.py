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

def create_new_model():
    print("Create a new model:")
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    agency_name = input("Enter the Model Agency's name: ")
    local_magazine_name = input("Enter the Magazine's name (or leave empty for none): ")
    photo_shoots = int(input("Enter the number of photo shoots: "))

    agency = session.query(ModelAgency).filter_by(name=agency_name).first()

    if not agency:
        print(f"No such Model Agency: {agency_name}")
        return

    local_magazine = None
    if local_magazine_name:
        local_magazine = session.query(LocalMagazine).filter_by(name=local_magazine_name).first()
        if not local_magazine:
            print(f"No such Magazine: {local_magazine_name}")
            return

    new_model = Model(first_name=first_name, last_name=last_name, agency=agency, local_magazine=local_magazine, photo_shoots=photo_shoots)
    session.add(new_model)
    session.commit()

    print(f"New model {first_name} {last_name} created successfully!")

def update_model():
    model_id = int(input("Enter the ID of the model you want to update: "))
    model = session.query(Model).filter_by(id=model_id).first()

    if not model:
        print(f"No model found with ID {model_id}")
        return

    print(f"Updating model: {model.first_name} {model.last_name}")

    first_name = input("Enter the updated first name (or leave empty to keep current): ")
    last_name = input("Enter the updated last name (or leave empty to keep current): ")
    agency_name = input("Enter the updated Model Agency's name (or leave empty to keep current): ")
    local_magazine_name = input("Enter the updated Magazine's name (or leave empty for none): ")
    photo_shoots = int(input("Enter the updated number of photo shoots: "))

    if first_name:
        model.first_name = first_name
    if last_name:
        model.last_name = last_name

    if agency_name:
        agency = session.query(ModelAgency).filter_by(name=agency_name).first()
        if not agency:
            print(f"No such Model Agency: {agency_name}")
            return
        model.agency = agency

    if local_magazine_name:
        local_magazine = session.query(LocalMagazine).filter_by(name=local_magazine_name).first()
        if not local_magazine:
            print(f"No such Magazine: {local_magazine_name}")
            return
        model.local_magazine = local_magazine

    model.photo_shoots = photo_shoots
    session.commit()

    print(f"Model {model_id} updated successfully!")

def get_models_under_agency(agency_name):
    models = (
        session.query(Model)
        .join(ModelAgency)
        .filter(ModelAgency.name == agency_name)
        .all()
    )
    return models

def get_models_for_magazine(magazine_name):
    models = (
        session.query(Model)
        .join(LocalMagazine)
        .filter(LocalMagazine.name == magazine_name)
        .all()
    )
    return models

def get_eligible_models():
    eligible_models = (
        session.query(Model)
        .filter(Model.photo_shoots >= 10)
        .all()
    )
    return eligible_models
