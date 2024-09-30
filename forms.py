from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    date = DateTimeField('Date', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    attendees = IntegerField('Number of Attendees', validators=[DataRequired()])
    submit = SubmitField('Create Event')
