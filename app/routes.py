from flask import render_template, request, flash, url_for, redirect, session
from app import app
from app.models import Client, Material, Cross, db
from app.forms import LoginForm, ClientForm, OrderForm, ProductForm, AddsForm, PathForm, WritingForm, HeadForm, MaterialForm, HeadsForm, CrossForm, WazonForm, PhotoForm, PodstForm, LettersForm, LampionForm
from sqlalchemy import create_engine
import functools
from io import BytesIO
from base64 import b64encode, b64decode

def login_required(view_func):
    @functools.wraps(view_func)
    def check_permissions(*args, **kwargs):
        if session.get('logged_in'):
            return view_func(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return check_permissions

def entrys(form, klient_id=None, klient=None):
   if form.validate_on_submit():
      if klient_id == None:
         klient = Client(
            name=form.name.data,
            surname=form.surname.data,
            tel1=form.tel1.data,
            tel2=form.tel2.data,
            loc=form.loc.data,
            info=form.info.data
         )
         db.session.add(klient)
      else:
         form.populate_obj(klient)
      db.session.commit()
   else:
      errors = form.errors

@app.route("/")
def index():
   all_klients = Client.query

   return render_template("homepage.html", all_klients=all_klients)

@app.route("/details/<int:entry_id>/")
@login_required
def klient_details(entry_id):
   klient = Client.query.filter_by(id=entry_id).first_or_404()
   errors = None
   return render_template("details.html", klient=klient, errors=errors)

@app.route("/new-post/", methods=["GET", "POST"])
@login_required
def create_entry():
   form = ClientForm()
   errors = None
   if request.method == 'POST':
      entrys(form)
      return redirect(url_for('index'))

   return render_template("entry_form.html", form=form, errors=errors)

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_entry(entry_id):
   entry = Client.query.filter_by(id=entry_id).first_or_404()
   form = ClientForm(obj=entry)
   errors = None
   if request.method == 'POST':
      entrys(form, klient_id=entry_id, klient=entry)
      return redirect(url_for('index'))

   return render_template("entry_form.html", form=form, errors=errors)

@app.route("/login/", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   errors = None
   next_url = request.args.get('next')
   if request.method == 'POST':
      if form.validate_on_submit():
         session['logged_in'] = True
         session.permanent = True  # Use cookie to store session.
         flash('You are now logged in.', 'success')
         return redirect(next_url or url_for('index'))
      else:
         errors = form.errors
   return render_template("login_form.html", form=form, errors=errors)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
   if request.method == 'POST':
      session.clear()
      flash('You are now logged out.', 'success')
   return redirect(url_for('index'))


      
@app.route("/<int:entry_id>", methods=['POST', 'GET'])
@login_required
def delete_entry(entry_id):
   entry = Client.query.filter_by(id=entry_id).first_or_404()
   db.session.delete(entry)
   db.session.commit()
      
   all_klients = Client.query

   return render_template("homepage.html", all_klients=all_klients)

@app.route("/dodatki")
def dodatki():

   return render_template("dodatki.html")

@app.route("/materials")
def material_list():
   all_materials = Material.query
     
   return render_template("materials.html", all_materials=all_materials)

def entrymat(form, material_id=None, material=None):
   if form.validate_on_submit():
      f = request.files['photo']
      if material_id == None:
         material = Material(
            name=form.name.data,
            price=form.price.data,
            info=form.info.data,
            photo=f.read()
         )
         db.session.add(material)
      else:
         form.populate_obj(material)
      db.session.commit()
   else:
      errors = form.errors


@app.route("/materials")
def get_mat(entry_id):
   images = Material.query.get_or_404(entry_id)
   image = b64decode(images.photo)
   return image

@app.route("/materials/<int:entry_id>", methods=['POST', 'GET'])
@login_required
def delete_mat(entry_id):
   mentry = Material.query.filter_by(id=entry_id).first_or_404()
   db.session.delete(mentry)
   db.session.commit()
      
   all_materials = Material.query
   
   return render_template("materials.html", all_materials=all_materials)

@app.route("/add_mat/", methods=["GET", "POST"])
@login_required
def add_mat():
   form = MaterialForm()
   errors = None
   if request.method == 'POST':
      entrymat(form)
      return redirect(url_for('material_list'))

   return render_template("add_mat.html", form=form, errors=errors)

@app.route("/krzyze")
def krzyz_list():
   all_krzyz = Cross.query
   
   return render_template("krzyze.html", all_krzyz=all_krzyz)

def entrykrz(form, krzyz_id=None, krzyz=None):
   if form.validate_on_submit():
      if krzyz_id == None:
         krzyz = Cross(
            name=form.name.data,
            price=form.price.data,
         )
         db.session.add(krzyz)
      else:
         form.populate_obj(krzyz)
      db.session.commit()
   else:
      errors = form.errors

@app.route("/krzyze/<int:entry_id>", methods=['POST', 'GET'])
@login_required
def delete_krz(entry_id):
   kentry = Cross.query.filter_by(id=entry_id).first_or_404()
   db.session.delete(kentry)
   db.session.commit()
      
   all_krzyz = Cross.query
   
   return render_template("krzyze.html", all_krzyz=all_krzyz)

@app.route("/add_krz/", methods=["GET", "POST"])
@login_required
def add_krz():
   form = CrossForm()
   errors = None
   if request.method == 'POST':
      entrykrz(form)
      return redirect(url_for('krzyz_list'))

   return render_template("add_krzyz.html", form=form, errors=errors)