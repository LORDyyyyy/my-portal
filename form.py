from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FieldList
from wtforms.validators import DataRequired, Length
from wtforms.validators import Email, Optional, URL, EqualTo
from flask_wtf.file import FileField, FileAllowed


class RegistrationStudent(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(),
                            Length(min=2, max=15)])
    middleName = StringField('Middle Name')
    lastName = StringField('Last Name', validators=[DataRequired(),
                           Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')
                                                 ]
                                     )
    submit = SubmitField('Submit')


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationTeacher(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(),
                            Length(min=2, max=15)])
    lastName = StringField('Last Name', validators=[DataRequired(),
                           Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')
                                                 ]
                                     )
    submit = SubmitField('Submit')


class Student_SubjectForm(FlaskForm):
    subjectCode = StringField('Subject Code', validators=[DataRequired()])
    submit = SubmitField('Join Subject')


class Teacher_SubjectForm(FlaskForm):
    subjectName = StringField('Subject Name', validators=[DataRequired()])
    emails = FieldList(StringField('Teacher Email',
                       validators=[Email(), Optional()]),
                       min_entries=0)
    books = FieldList(StringField('Google Drive Book link',
                                  validators=[Optional(), URL()]),
                      min_entries=0)
    submit = SubmitField('Submit')


class resetPass(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confrimPassword = PasswordField(
        'confrim password', validators=[DataRequired()])
    submit = SubmitField('submit')


class Forgotpass(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('submit')


class Verify(FlaskForm):
    verifyCode = StringField('code', validators=[DataRequired()])
    submit = SubmitField('submit')


class VerifyRegister(FlaskForm):
    verification_code = StringField(
        'Verification Code', validators=[DataRequired()])
    submit = SubmitField('submit')


class SendNews(FlaskForm):
    message = StringField('Send Message', validators=[DataRequired()])
    submit = SubmitField('Send')


class edit_profile(FlaskForm):
    Photo = FileField('Photo', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'],
                    'Only JPEG and PNG images are allowed.')
    ])
    submit = SubmitField('Update Profile')


class UploadPDF(FlaskForm):
    pdf_slide = FileField('Slide File',
                          validators=[DataRequired(), FileAllowed(
                              ['pdf', 'pptx', 'ppt'],
                              'Only PDF and PPT files are allowed.')
                          ]
                          )
    pdf_sheet = FileField('Sheet File',
                          validators=[DataRequired(), FileAllowed(
                              ['pdf', 'pptx', 'ppt'],
                              'Only PDF and PPT files are allowed.')
                          ]
                          )
