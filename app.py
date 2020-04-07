from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from config import Development, Production

# create an instance of class Flask called app
app = Flask(__name__)
app.config.from_object(Development)
# app.config.from_object(Production)

# create an instance of sqlalchemy
db = SQLAlchemy(app)

from models.doto import DotoModel

# create tables in our database
@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/todo')
def todo():
    activities = DotoModel.fetch_records()
    return render_template('todo.html', activities=activities)


@app.route('/new_activity', methods=['POST'])
def new_activity():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        activity = request.form['activity']

        new = DotoModel(name=name, email=email, activity=activity)
        new.add_records()

    return redirect(url_for('todo'))


@app.route('/update_information/<int:id>', methods=['POST'])
def update_information(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        activity = request.form['activity']

        DotoModel.update_by_id(id=id, name=name, email=email, activity=activity)

    return redirect(url_for('todo'))


if __name__ == '__main__':
    app.run()
