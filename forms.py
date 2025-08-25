
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired





class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')



class AddStudentForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    dbms=IntegerField('dbms',validators=[DataRequired()])
    coa=IntegerField('coa',validators=[DataRequired()])
    iwt=IntegerField('iwt',validators=[DataRequired()]) 
    ds=IntegerField('ds',validators=[DataRequired()])
    cpp=IntegerField('cpp',validators=[DataRequired()])
    submit = SubmitField('Add Student')
class ChangePasswordForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    submit = SubmitField('Change Password')

    