from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import Length, URL

class TwitterUserForm(FlaskForm):
    TwitterUsername = StringField('Enter Username')
    submit = SubmitField('Submit')

class TwitterContentForm(FlaskForm):
    TwitterTopic = StringField('Enter Twitter Topic')
    submit = SubmitField('Submit')
