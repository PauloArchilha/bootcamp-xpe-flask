import os
from flask import Flask, render_template
from form import NameForm
from flask_migrate import Migrate
from models.User import db


app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = " "
    return render_template('index.html', name=name, form=form)
