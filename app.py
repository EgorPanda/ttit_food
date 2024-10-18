from flask import Flask, render_template, request, redirect
from db import db  
from models import Recipe

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)


@app.route('/')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)


@app.route('/add', methods=['POST'])
def add_recipe():
    title = request.form['title']
    description = request.form['description']
    new_recipe = Recipe(title=title, description=description)
    
    db.session.add(new_recipe)
    db.session.commit()
    
    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True, host='0.0.0.0')
