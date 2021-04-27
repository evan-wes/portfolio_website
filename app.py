from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager

app = Flask(__name__)
if environ.get('DATABASE_URL') is None:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL').replace('postgres', 'postgresql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'

db = SQLAlchemy(app)
#login = LoginManager(app)

import routes

if environ.get('DATABASE_URL') is None:

    from models import Project

    # Create database and add projects
    db.drop_all()
    db.create_all()

    # Create Project instances
    naive_bayes_sklearn_project = Project(id_name='naive_bayes_sklearn',
                                            name='Naive-Bayes Classifcation with sklearn',
                                            tags='sklearn classification supervised-ML Naive-Bayes',
                                            html_filename='naive_bayes_sklearn.html',
                                            heroku_link='https://naive-bayes-sklearn.herokuapp.com/')

    # Add Project instances to database
    db.session.add(naive_bayes_sklearn_project)

    # Commit changes to database
    db.session.commit()
