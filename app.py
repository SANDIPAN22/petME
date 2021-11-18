from flask import Flask, redirect, url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import form
from forms import AddForm,DeleteForm,Attach
import os

from flask_sqlalchemy.model import Model
from sqlalchemy.orm import backref

app=Flask(__name__)

db_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"pet.db")

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+db_path
app.config['SECRET_KEY']="asasdsaasc"

db=SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(10),nullable=False)
    age=db.Column(db.Integer)
    owner=db.relationship('Owner', backref='puppy',uselist=False)

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        print(self.owner)
        if self.owner:
            return f"The Puppy name is: {self.name} and owned by {self.owner.name}"
        else:
            return f"The Puppy name is: {self.name}. No owner yet !"

class Owner(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20),nullable=False)
    puppy_id=db.Column(db.Integer, db.ForeignKey('puppy.id'))
    def __init__(self,name,pid):
        self.name=name
        self.puppy_id=pid

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add',methods=['GET','POST'])
def addp():
    form=AddForm()
    if form.validate_on_submit():
        
        p=Puppy(form.name.data,form.age.data)
        db.session.add(p)
        db.session.commit()
        print("maal dhuklooo")
        return redirect (url_for('show'))
    return render_template('add.html',form=form)

@app.route('/show')
def show():
    pp=Puppy.query.all()
    print(pp)
    return render_template('show.html',pp=pp)
@app.route('/del',methods=['POST','GET'])
def delp():
    form=DeleteForm()
    if form.validate_on_submit():
        p=Puppy.query.get(form.pid.data)
        db.session.delete(p)
        db.session.commit()
        return redirect (url_for('show'))
    return render_template('del.html',form=form)

@app.route('/attach',methods=['GET','POST'])
def attach():
    form=Attach()
    if form.validate_on_submit():
        o=Owner(form.name.data,form.pid.data)
        db.session.add(o)
        db.session.commit()
        return redirect (url_for('show'))
    return render_template('attach.html',form=form)
        
if __name__=="__main__":
    app.run(debug=True)