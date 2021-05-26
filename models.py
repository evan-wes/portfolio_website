from app import db

# Define project_html model:
class Project(db.Model):
    id_name = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    tags = db.Column(db.String)
    html_filename = db.Column(db.String, unique=True, nullable=False)
    github_repo = db.Column(db.String, unique=True, nullable=False)
    heroku_link = db.Column(db.String, unique=True, nullable=True)
