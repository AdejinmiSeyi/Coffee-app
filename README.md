# Coffee Shop App

## Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. 

The application is able to:

Display graphics representing the ratios of ingredients in each drink.
Allow public users to view drink names and graphics.
Allow the shop baristas to see the recipe information.
Allow the shop managers to create new drinks and edit existing drinks.

# Coffee Shop Backend
## Getting Started
### Installing Dependencies
#### Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs

#### Virtual Environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the python docs

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

pip install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

##### Key Dependencies
Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy and Flask-SQLAlchemy are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in ./src/database/models.py. We recommend skimming this code first so you know how to interface with the Drink model.

jose JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server
From within the ./src directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

``` bash
export FLASK_APP=api.py;
``` 

To run the server, execute:
``` bash
flask run --reload
```

The --reload flag will detect file changes and restart the server automatically.


