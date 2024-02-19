from cli import list_models_under_agency, list_models_for_magazine, list_eligible_models

def main():
    print("Welcome to Model Hub!")
    while True:
        print("Options:")
        print("1. List models under an agency")
        print("2. List models for a magazine")
        print("3. List models eligible for international magazines")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            list_models_under_agency()
        elif choice == '2':
            list_models_for_magazine()
        elif choice == '3':
            list_eligible_models()
        elif choice == '4':
            print("Exiting Model Hub. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()


