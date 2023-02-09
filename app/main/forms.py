from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    role = SelectField(_l('Position'), choices=[
                       ('End User'), ('VAO'), ('RI'), ('HQDT'), ('Tahsildar')])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    file = FileField(_l('Upload Certificate'),validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class ApprovalForm(FlaskForm):
    approval_by_vao = SelectField(_l('Approval Status by VAO'), choices=[('Yet to Review'), ('Approved'), ('Rejected')])
    reason_by_vao = TextAreaField(_l('Reason by VAO'))
    approval_by_ri = SelectField(_l('Approval Status by RI'), choices=[
                                 ('Yet to Review'), ('Approved'), ('Rejected')])
    reason_by_ri = TextAreaField(_l('Reason by RI'))
    approval_by_hqdt = SelectField(_l('Approval Status by HQDT'), choices=[
                                   ('Yet to Review'), ('Approved'), ('Rejected')])
    reason_by_hqdt = TextAreaField(_l('Reason by HQDT'))
    approval_by_Tahsildar = SelectField(_l('Approval Status by Tahsildar'), choices=[
                                        ('Yet to Review'), ('Approved'), ('Rejected')])
    reason_by_Tahsildar = TextAreaField(_l('Reason by Tahsildar'))
    submit = SubmitField(_l('Submit'))


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))
