from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
	title = StringField("title",validators=[Required()])
	pitch = TextAreaField("pitch",validators=[Required()])
	category = RadioField('Label', choices=[('promotionpitch','promotionpitch'), ('interviewpitch','interviewpitch'),('pickuplines','pickuplines'),('productpitch','productpitch')],validators=[Required()])
	submit = SubmitField('submit')

class CommentForm(FlaskForm):
	description = TextAreaField('',validators=[Required()])
	submit = SubmitField() 

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()
	