from flask import render_template, json
import os
from app import app

@app.route('/')
@app.route('/index')
def index():

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

    return render_template('index.html',
                            workexperience=workexperience,
                            skills=skills,
                            degrees=degrees)   

  