from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class AccountForm(FlaskForm):
    name = StringField("Account name",validators=[DataRequired()])
    submit = SubmitField("Create Account")