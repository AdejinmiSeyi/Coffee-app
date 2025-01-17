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

``` bash
pip install -r requirements.txt
```
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

# Coffee Shop Frontend

## Getting Setup

> _tip_: this frontend is designed to work with [Flask-based Backend](../backend). It is recommended you stand up the backend first, test using Postman, and then the frontend should integrate smoothly.

### Installing Dependencies

#### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

#### Installing Ionic Cli

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI is in the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

#### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

> _tip_: **npm i** is shorthand for **npm install**



