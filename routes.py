from flask import request, render_template, flash, redirect, url_for
from models import Project
from app import app, db

# Route for the home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('landing_page.html', tab_title='Home')

# Route for the background page
@app.route('/background')
def background():
    return render_template('background.html', tab_title='Background')

# Route for the projects page
@app.route('/projects')
def projects():
    return render_template('projects.html', tab_title='Projects')

# Route for individual project pages
@app.route('/projects/<string:id_name>')
def project_page(id_name):
    # Query Project table for specific project using the 'id_name' primary key 
    project = Project.query.filter_by(id_name = id_name).first_or_404(description="No project by that name")
    # Render the 'project_page' template with relevant project passed in
    return render_template('project_page.html', project=project)


# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html', tab_title='Contact')