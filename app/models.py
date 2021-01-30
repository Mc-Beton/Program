from . import db
import datetime

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname=db.Column(db.String(80), nullable=False)
    tel1=db.Column(db.String(80), nullable=False)
    tel2=db.Column(db.String(80), nullable=False)
    loc=db.Column(db.String(80), nullable=False)
    info = db.Column(db.Text, nullable=False)
    #pub_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
   

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price=db.Column(db.String(80), nullable=False)
    info=db.Column(db.Text)
    photo=db.Column(db.String(80))
    

class Cross(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price=db.Column(db.String(80), nullable=False)
    photo=db.Column(db.String(80))

class Headskop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    photo=db.Column(db.String(80), nullable=False)

class Headskla(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    photo=db.Column(db.String(80), nullable=False)

class Letters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price=db.Column(db.String(80), nullable=False)
    photo=db.Column(db.String(80))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    adds_id = db.Column(db.Integer, db.ForeignKey('adds.id'))
    finish_id = db.Column(db.Integer, db.ForeignKey('finish.id'))
    head_id = db.Column(db.Integer, db.ForeignKey('head.id'))
    writing_id = db.Column(db.Integer, db.ForeignKey('writing.id'))
    info=db.Column(db.Text)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(80), nullable=False)
    finish=db.Column(db.String(80))
    parapet=db.Column(db.String(80))
    mat1=db.Column(db.String(80))
    cokoly=db.Column(db.String(80))
    mat2=db.Column(db.String(80))
    plyta=db.Column(db.String(80))
    thick=db.Column(db.String(80))
    mat3=db.Column(db.String(80))
    info=db.Column(db.Text)

class Adds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wazon = db.Column(db.Boolean)
    info1=db.Column(db.Text)
    podstawa=db.Column(db.Boolean)
    info2=db.Column(db.Text)
    lampion=db.Column(db.Boolean)
    info3=db.Column(db.Text)
    photo=db.Column(db.Boolean)
    info4=db.Column(db.Text)
    cross=db.Column(db.Boolean)
    info5=db.Column(db.Text)
    
class Path(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String(80))
    border=db.Column(db.String(80))
    info=db.Column(db.Text)

class Writing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    kind=db.Column(db.String(80))
    info=db.Column(db.Text)

class Head(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thick=db.Column(db.String(80))
    mat1 = db.Column(db.String(80))
    mat2=db.Column(db.String(80))
    info=db.Column(db.Text)

class Wazon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price=db.Column(db.String(80), nullable=False)

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price=db.Column(db.String(80), nullable=False)

class Podst(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price=db.Column(db.String(80), nullable=False)

class Lampion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price=db.Column(db.String(80), nullable=False)
    photo=db.Column(db.Text)