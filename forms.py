from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import InputRequired

class AddForm(FlaskForm):
    name=StringField("Write the name of the Puppy !")
    age=IntegerField("What is the age ?")
    submit=SubmitField("Enter")

class DeleteForm(FlaskForm):
    pid=IntegerField("Enter the puppy id:")
    submit=SubmitField("Delete !")

class Attach(FlaskForm):
    name=StringField("Enter the name of the Owner")
    pid=IntegerField("Enter the puppy id to adopt")
    submit=SubmitField("Adopt Now!")