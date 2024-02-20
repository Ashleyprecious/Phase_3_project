# lib/model_hub/main.py
from cli import list_models_under_agency, list_models_for_magazine, list_eligible_models, create_new_model

def main():
    print("Welcome to Model Hub!")
    while True:
        print("Options:")
        print("1. List models under an agency")
        print("2. List models for a magazine")
        print("3. List models eligible for international magazines")
        print("4. Create a new model")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            list_models_under_agency()
        elif choice == '2':
            list_models_for_magazine()
        elif choice == '3':
            list_eligible_models()
        elif choice == '4':
            create_new_model()
        elif choice == '5':
            print("Exiting Model Hub. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()
