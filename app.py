from flask import Flask, url_for
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landingpage.html')

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/create_project')
def create_project():
    return render_template('new_project.html')

@app.route('/list_projects')
def list_projects():
    return render_template('listed_projects.html')

@app.route('/projects_details')
def list_projects_details():
    return render_template('listed_project_detail.html')

if __name__=='__main__':
    app.run(debug=True)