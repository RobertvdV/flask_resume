import os

from flask import render_template, json, send_from_directory
from app import app
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')   

@bp.route("/download/<path:filename>")
def download(filename):
    filepath = os.path.join(app.static_folder, 'download/')
    return send_from_directory(filepath, filename, as_attachment=True)  

@bp.route('/resume')
def resume():

    # Working Experience
    filename = os.path.join(app.static_folder, 'json/workexperience.json')
    with open(filename) as f:
        workexperience = json.load(f)

    # Skills
    filename = os.path.join(app.static_folder, 'json/skills.json')
    with open(filename) as f:
        skills = json.load(f)
        skills = {k: v for k, v in sorted(skills.items(), key=lambda item: item[1], reverse=True)}
    
    # Degrees
    filename = os.path.join(app.static_folder, 'json/degrees.json')
    with open(filename) as f:
        degrees = json.load(f)

    return render_template('resume.html',
                            workexperience=workexperience,
                            skills=skills,
                            degrees=degrees)   

@bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')
