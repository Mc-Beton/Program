from flask import render_template, request, flash, url_for, redirect, session
from app import app
from app.models import Photo, Client, Material, Cross, Headskop, Headskla, Letters, db
from app.forms import HeadsklaForm, HeadskopForm, LoginForm, ClientForm, OrderForm, ProductForm, AddsForm, PathForm, WritingForm, HeadForm, MaterialForm, CrossForm, WazonForm, PhotoForm, PodstForm, LettersForm, LampionForm
from sqlalchemy import create_engine
import functools
from io import BytesIO
from base64 import b64encode, b64decode
from appiq import mat


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

@app.route("/baza")
def dodatki():

   return render_template("dodatki.html")





#Cross
@app.route("/baza/krzyze")
def krzyz_list():
   all_krzyz = Cross.query
   
   return render_template("krzyze.html", all_krzyz=all_krzyz)

def entrykrz(form, krzyz_id=None, krzyz=None):
   if form.validate_on_submit():
      if krzyz_id == None:
         krzyz = Cross(
            name=form.name.data,
            price=form.price.data,
            photo=form.photo.data
         )
         db.session.add(krzyz)
      else:
         form.populate_obj(krzyz)
      db.session.commit()
   else:
      errors = form.errors

@app.route("/baza/krzyze/<int:entry_id>", methods=['POST', 'GET'])
@login_required
def delete_krz(entry_id):
   kentry = Cross.query.filter_by(id=entry_id).first_or_404()
   db.session.delete(kentry)
   db.session.commit()
      
   all_krzyz = Cross.query
   
   return render_template("krzyze.html", all_krzyz=all_krzyz)

@app.route("/baza/add_krz/", methods=["GET", "POST"])
@login_required
def add_krz():
   form = CrossForm()
   errors = None
   if request.method == 'POST':
      entrykrz(form)
      return redirect(url_for('krzyz_list'))

   return render_template("add_krzyz.html", form=form, errors=errors)

@app.route("/baza/edit-mat/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_krz(entry_id):
    mentry = Cross.query.filter_by(id=entry_id).first_or_404()
    form = CrossForm(obj=mentry)
    errors = None
    if request.method == 'POST':
        entrykrz(form, krzyz_id=entry_id, krzyz=mentry)
        return redirect(url_for('krzyz_list'))

    return render_template("add_krzyz.html", form=form, errors=errors)






#materials
@app.route("/baza/materials")
def material_list():
   all_materials = Material.query
     
   return render_template("materials.html", all_materials=all_materials)

def entrymat(form, material_id=None, material=None):
    if form.validate_on_submit():
        #f = request.files['photo']
        if material_id == None:
            material = Material(
                name=form.name.data,
                price=form.price.data,
                info=form.info.data,
                photo=form.photo.data
                #photo=f.read()
            )
            db.session.add(material)
        else:
            form.populate_obj(material)
        db.session.commit()
    else:
        errors = form.errors


#@app.route("/materials")
#def get_mat(entry_id):
#   images = Material.query.get_or_404(entry_id)
#   image = b64decode(images.photo)
#   return image

@app.route("/baza/materials/<int:entry_id>", methods=['POST', 'GET'])
@login_required
def delete_mat(entry_id):
   mentry = Material.query.filter_by(id=entry_id).first_or_404()
   db.session.delete(mentry)
   db.session.commit()
      
   all_materials = Material.query
   
   return render_template("materials.html", all_materials=all_materials)

@app.route("/baza/add_mat/", methods=["GET", "POST"])
@login_required
def add_mat():
   form = MaterialForm()
   errors = None
   if request.method == 'POST':
      entrymat(form)
      return redirect(url_for('material_list'))

   return render_template("add_mat.html", form=form, errors=errors)

@app.route("/baza/edit-mat/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_mat(entry_id):
    mentry = Material.query.filter_by(id=entry_id).first_or_404()
    form = MaterialForm(obj=mentry)
    errors = None
    if request.method == 'POST':
        entrymat(form, material_id=entry_id, material=mentry)
        return redirect(url_for('material_list'))

    return render_template("add_mat.html", form=form, errors=errors)

   


#Heads kopertowe
@app.route("/baza/wzory kopertowe")
def headskop_list():
   all_headskop = Headskop.query
   
   return render_template("kopertowe.html", all_headskop=all_headskop)

def entrykop(form, headskop_id=None, headskop=None):
   if form.validate_on_submit():
      if headskop_id == None:
         headskop = Headskop(
            name=form.name.data,
            photo=form.photo.data
         )
         db.session.add(headskop)
      else:
         form.populate_obj(headskop)
      db.session.commit()
   else:
      errors = form.errors

@app.route("/baza/kopertowe/<int:entry_id>", methods=['POST', 'GET'])
@login_required
def delete_kop(entry_id):
   kentry = Headskop.query.filter_by(id=entry_id).first_or_404()
   db.session.delete(kentry)
   db.session.commit()
      
   all_headskop = Headskop.query
   
   return render_template("kopertowe.html", all_headskop=all_headskop)

@app.route("/baza/kopertowe/add_kop/", methods=["GET", "POST"])
@login_required
def add_kop():
   form = HeadskopForm()
   errors = None
   if request.method == 'POST':
      entrykop(form)
      return redirect(url_for('headskop_list'))

   return render_template("add_kop.html", form=form, errors=errors)

@app.route("/baza/kopertowe/edit-kop/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_kop(entry_id):
    mentry = Headskop.query.filter_by(id=entry_id).first_or_404()
    form = HeadskopForm(obj=mentry)
    errors = None
    if request.method == 'POST':
        entrykop(form, headskop_id=entry_id, headskop=mentry)
        return redirect(url_for('headskop_list'))

    return render_template("add_kop.html", form=form, errors=errors)






#Heads klasyczne
@app.route("/baza/wzory klasyczne")
def headskla_list():
   all_headskla = Headskla.query
   
   return render_template("klasyczne.html", all_headskla=all_headskla)

def entrykla(form, headskla_id=None, headskla=None):
   if form.validate_on_submit():
      if headskla_id == None:
         headskla = Headskla(
            name=form.name.data,
            photo=form.photo.data
         )
         db.session.add(headskla)
      else:
         form.populate_obj(headskla)
      db.session.commit()
   else:
      errors = form.errors

@app.route("/baza/klasyczne/<int:entry_id>", methods=['POST', 'GET'])
@login_required
def delete_kla(entry_id):
   kentry = Headskla.query.filter_by(id=entry_id).first_or_404()
   db.session.delete(kentry)
   db.session.commit()
      
   all_headskla = Headskla.query
   
   return render_template("klasyczne.html", all_headskla=all_headskla)

@app.route("/baza/klasyczne/add_kla/", methods=["GET", "POST"])
@login_required
def add_kla():
   form = HeadsklaForm()
   errors = None
   if request.method == 'POST':
      entrykla(form)
      return redirect(url_for('headskla_list'))

   return render_template("add_kla.html", form=form, errors=errors)

@app.route("/baza/klasyczne/edit-kla/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_kla(entry_id):
    mentry = Headskla.query.filter_by(id=entry_id).first_or_404()
    form = HeadsklaForm(obj=mentry)
    errors = None
    if request.method == 'POST':
        entrykla(form, headskla_id=entry_id, headskla=mentry)
        return redirect(url_for('headskla_list'))

    return render_template("add_kla.html", form=form, errors=errors)







#Letters
@app.route("/baza/litery")
def letter_list():
   all_letter = Letters.query
   
   return render_template("litery.html", all_letter=all_letter)

def entrylet(form, letter_id=None, letter=None):
   if form.validate_on_submit():
      if letter_id == None:
         letter = Letters(
            name=form.name.data,
            price=form.price.data,
            photo=form.photo.data
         )
         db.session.add(letter)
      else:
         form.populate_obj(letter)
      db.session.commit()
   else:
      errors = form.errors

@app.route("/baza/litery/<int:entry_id>", methods=['POST', 'GET'])
@login_required
def delete_let(entry_id):
   kentry = Letters.query.filter_by(id=entry_id).first_or_404()
   db.session.delete(kentry)
   db.session.commit()
      
   all_letter = Letters.query
   
   return render_template("litery.html", all_letter=all_letter)

@app.route("/baza/litery/add_let/", methods=["GET", "POST"])
@login_required
def add_let():
   form = LettersForm()
   errors = None
   if request.method == 'POST':
      entrylet(form)
      return redirect(url_for('letter_list'))

   return render_template("add_let.html", form=form, errors=errors)

@app.route("/baza/litery/edit-let/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_let(entry_id):
    mentry = Letters.query.filter_by(id=entry_id).first_or_404()
    form = LettersForm(obj=mentry)
    errors = None
    if request.method == 'POST':
        entrylet(form, letter_id=entry_id, letter=mentry)
        return redirect(url_for('letter_list'))

    return render_template("add_let.html", form=form, errors=errors)




#new order
@app.route("/new-order")
@login_required
def new_order():

   return render_template("new_order.html")

@app.route("/new-order/wzory-klasyczne")
def poj_kla():
   wzory = Headskla.query
   
   return render_template("poj.html", wzory=wzory)

@app.route("/new-order/wzory-kopertowe")
def poj_kop():
   wzory = Headskop.query
   
   return render_template("poj.html", wzory=wzory)

@app.route("/new-order/<int:entry_id>")
def poj_details(entry_id):
   
   return render_template("poj_details.html")





#Zdjęcia
@app.route("/baza/zdjecia")
def photo_list():
   lista = Photo.query
   
   return render_template("zdjecia.html", lista=lista)

def entrypho(form, photo_id=None, photo=None):
   if form.validate_on_submit():
      if photo_id == None:
         photo = Photo(
            name=form.name.data,
            price=form.price.data
         )
         db.session.add(photo)
      else:
         form.populate_obj(photo)
      db.session.commit()
   else:
      errors = form.errors

@app.route("/baza/zdjecia/<int:entry_id>", methods=['POST', 'GET'])
@login_required
def delete_pho(entry_id):
   kentry = Photo.query.filter_by(id=entry_id).first_or_404()
   db.session.delete(kentry)
   db.session.commit()
      
   lista = Photo.query
   
   return render_template("zdjecia.html", lista=lista)

@app.route("/baza/add_pho/", methods=["GET", "POST"])
@login_required
def add_pho():
   form = PhotoForm()
   errors = None
   if request.method == 'POST':
      entrypho(form)
      return redirect(url_for('photo_list'))

   return render_template("add_photo.html", form=form, errors=errors)

@app.route("/baza/edit-photo/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit_pho(entry_id):
    mentry = Photo.query.filter_by(id=entry_id).first_or_404()
    form = PhotoForm(obj=mentry)
    errors = None
    if request.method == 'POST':
        entrypho(form, photo_id=entry_id, photo=mentry)
        return redirect(url_for('photo_list'))

    return render_template("add_photo.html", form=form, errors=errors)