from werkzeug.routing import ValidationError
from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, TextAreaField, BooleanField, FileField
from wtforms.validators import DataRequired
from config import Config
from app.models import Photo, Cross, Material, Lampion, Wazon, Podst, Letters
from wtforms_sqlalchemy.fields import QuerySelectField

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

def photo_query():
   return Photo.query

def cross_query():
   return Cross.query

def mat_query():
    return Material.query

def let_query():
    return Letters.query

def wazon_query():
    return Wazon.query

def podst_query():
    return Podst.query

def lampion_query():
    return Lampion.query


class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    tel1 = StringField('Tel1', validators=[DataRequired()])
    tel2 = StringField('Tel2')
    loc = StringField('Loc')
    info = TextAreaField('Info')
    zal = StringField('zaliczka')
    pri = StringField('Cena')

class OrdersForm(FlaskForm):
    info = TextAreaField('Info')

class ProductForm(FlaskForm):
    kind = StringField('Kind', validators=[DataRequired()])
    finish = StringField('Finish', validators=[DataRequired()])
    parapet = StringField('Parapet', validators=[DataRequired()])
    mat1 = QuerySelectField(query_factory=mat_query, allow_blank=True, get_label='name')
    cokoly = StringField('Cokoly', validators=[DataRequired()])
    mat2 = QuerySelectField(query_factory=mat_query, allow_blank=True, get_label='name')
    plyta = StringField('Plyta', validators=[DataRequired()])
    thick = StringField('Thick', validators=[DataRequired()])
    mat3 = QuerySelectField(query_factory=mat_query, allow_blank=True, get_label='name')
    info11 = TextAreaField('Info')
    
class AddsForm(FlaskForm):
    wazon = QuerySelectField(query_factory=wazon_query, allow_blank=True, get_label='name')
    info1 = TextAreaField('Info')
    podstawa = QuerySelectField(query_factory=podst_query, allow_blank=True, get_label='name')
    info2 = TextAreaField('Info')
    lampion = QuerySelectField(query_factory=lampion_query, allow_blank=True, get_label='name')
    info3 = TextAreaField('Info')
    photo = QuerySelectField(query_factory=photo_query, allow_blank=True, get_label='name')
    info4 = TextAreaField('Info')
    cross = QuerySelectField(query_factory=cross_query, allow_blank=True, get_label='name')
    info5 = TextAreaField('Info')

class PathForm(FlaskForm):
    kind2 = TextAreaField('Kind')
    border = TextAreaField('Border')
    bench = TextAreaField('Bench')
    info8 = TextAreaField('Info')

class WritingForm(FlaskForm):
    content = TextAreaField('Content')
    kind3 = QuerySelectField(query_factory=let_query, allow_blank=True, get_label='name')
    info7 = TextAreaField('Info')

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
    dim1 = StringField('dim1')
    mat4 = QuerySelectField(query_factory=mat_query, allow_blank=True, get_label='name')
    dim2 = StringField('dim2')
    mat5 = QuerySelectField(query_factory=mat_query, allow_blank=True, get_label='name')
    info6 = TextAreaField('Info')