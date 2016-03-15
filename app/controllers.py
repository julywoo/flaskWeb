from database import init_db,db_session
from flask import Flask,request,session,redirect,url_for,abort,render_template,flash
from models import User,Post

from app import app

#main page
@app.route('/')
@app.route('/index')
def index():
    users=User.query.all()
    return render_template('index.html',users=users)