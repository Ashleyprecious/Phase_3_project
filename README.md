**MODEL HUB**
Model Hub is a command-line interface (CLI) program designed to help model agencies manage their models and provide information to magazine companies. It allows model agencies to track models, their assignments, and eligibility for international magazines.

**Problem Statement**
Model agencies often face challenges in tracking models and managing their experience levels. Similarly, upcoming models struggle to find a marketing platform and agents to enhance their careers. Magazine companies require information on models' experience levels to collaborate effectively.

**Solution**
Model Hub provides a CLI to address these challenges, offering the following features:

Model agencies can track their models, view assigned magazine companies, and identify models eligible for international collaborations.
Magazine companies can obtain information on models assigned to them.
**Features**
List models under a model agency.
List models assigned to a magazine.
List models eligible for international magazines.
Create a new model.
Update an existing model.

Directory Structure
lib/model_hub/
models.py: Defines the SQLAlchemy models (ModelAgency, Model, LocalMagazine).
cli.py: Contains CLI functions for interacting with the database.
main.py: Main program with user interaction options.
seeds.py: Seeds initial data into the database.
Setup
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the main program:

bash
Copy code
python main.py
Follow the CLI prompts to interact with the program.

Database
The program uses an SQLite database (model_hub.db) to store model agency, model, and local magazine information.

Seeding Data
To seed initial data into the database:

bash
Copy code
python seeds.py
Notes
Make sure to create a virtual environment and install the required dependencies from requirements.txt.
Update the DATABASE_URL in database.py if necessary.
Run main.py before seeding data using seeds.py.
Ensure correct file paths and permissions for SQLite database creation.
