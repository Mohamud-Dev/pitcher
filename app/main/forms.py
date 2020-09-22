from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
	body = TextAreaField("Add pitch",validators=[Required()])
	category = RadioField('Label', choices=[('pickup lines','pickup lines'), ('interview pitch','interview pitch'),('product pitch','product pitch'),('promotion pitch','promotion pitch')])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	body = TextAreaField('',validators=[Required()])
	submit = SubmitField() 