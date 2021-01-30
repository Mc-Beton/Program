from werkzeug.routing import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, FileField
from wtforms.validators import DataRequired
from config import Config

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate_username(self, field):
        if field.data != Config.ADMIN_USERNAME:
            raise ValidationError("Invalid username")
        return field.data

    def validate_password(self, field):
        if field.data != Config.ADMIN_PASSWORD:
            raise ValidationError("Invalid password")
        return field.data

class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    tel1 = StringField('Tel1', validators=[DataRequired()])
    tel2 = StringField('Tel2')
    loc = StringField('Loc')
    info = TextAreaField('Info')

class OrderForm(FlaskForm):
    info = TextAreaField('Info')

class ProductForm(FlaskForm):
    kind = StringField('Kind', validators=[DataRequired()])
    finish = StringField('Finish', validators=[DataRequired()])
    parapet = StringField('Parapet', validators=[DataRequired()])
    mat1 = StringField('Mat1', validators=[DataRequired()])
    cokoly = StringField('Cokoly', validators=[DataRequired()])
    mat2 = StringField('Mat2', validators=[DataRequired()])
    plyta = StringField('Plyta', validators=[DataRequired()])
    thick = StringField('Thick', validators=[DataRequired()])
    mat3 = StringField('Mat3', validators=[DataRequired()])
    info = TextAreaField('Info')
    
class AddsForm(FlaskForm):
    wazon = BooleanField('Wazon')
    info = TextAreaField('Info')
    podstawa = BooleanField('Podstawa')
    info = TextAreaField('Info')
    lampion = BooleanField('Lampion')
    info = TextAreaField('Info')
    photo = BooleanField('Photo')
    info = TextAreaField('Info')
    cross = BooleanField('Cross')
    info = TextAreaField('Info')

class PathForm(FlaskForm):
    kind = TextAreaField('Kind')
    border = TextAreaField('Border')
    info = TextAreaField('Info')

class WritingForm(FlaskForm):
    content = TextAreaField('Content')
    kind = TextAreaField('Kind')
    info = TextAreaField('Info')

class MaterialForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    price = TextAreaField('Price', validators=[DataRequired()])
    info = TextAreaField('Info')
    photo = TextAreaField('Photo')

class HeadskopForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    photo = TextAreaField('Photo')

class HeadsklaForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    photo = TextAreaField('Photo')

class CrossForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    price = TextAreaField('Price', validators=[DataRequired()])
    photo = TextAreaField('Photo')

class WazonForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    price = TextAreaField('Price', validators=[DataRequired()])

class PhotoForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    price = TextAreaField('Price', validators=[DataRequired()])

class PodstForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    price = TextAreaField('Price', validators=[DataRequired()])

class LettersForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    price = TextAreaField('Price', validators=[DataRequired()])
    photo = TextAreaField('Photo')

class LampionForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    price = TextAreaField('Price', validators=[DataRequired()])
    photo = TextAreaField('Photo')

class HeadForm(FlaskForm):
    thick = StringField('Thick', validators=[DataRequired()])
    mat1 = StringField('mat1')
    mat2 = StringField('mat2')
    info = TextAreaField('Info')