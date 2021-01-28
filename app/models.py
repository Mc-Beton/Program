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
    info=db.Column(db.Text, nullable=False)
    photo=db.Column(db.String(80))
    

class Cross(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price=db.Column(db.String(80), nullable=False)
    