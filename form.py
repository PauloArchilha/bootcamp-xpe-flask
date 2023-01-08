from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class NameForm(FlaskForm):
    name = StringField('Qual seu nome? ', validators=[DataRequired()])
    submit = SubmitField('submit')
