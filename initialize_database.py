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
                                        github_repo = 'https://github.com/evan-wes/naive_bayes_sklearn',
                                        heroku_link='https://naive-bayes-sklearn.herokuapp.com/')

okcupid_profile_analysis_project = Project(id_name='okcupid_profile_analysis',
                                            name='OKCupid Profile Analysis',
                                            tags='sklearn classification supervised-ML logistic-regression KNN decision-tree',
                                            html_filename='okcupid_profile_analysis.html',
                                            github_repo = 'https://github.com/evan-wes/OKCupid_Profile_Analysis',
                                            heroku_link='')

# Add Project instances to database
db.session.add(naive_bayes_sklearn_project)
db.session.add(okcupid_profile_analysis_project)

# Commit changes to database
db.session.commit()