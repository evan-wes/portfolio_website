from app import db
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