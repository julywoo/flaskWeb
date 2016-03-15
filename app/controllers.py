#coding:utf-8
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

#profile

@app.route('/profile/<int:userId>')
def profile(userId):
    #user information
    user =User.query.filter_by(id=userId).first()

    posts=Post.query.filter(Post.userid==User).order_by(Post.id.desc()).all()
    return render_template('profile.html',user=user,posts=posts,userId=userId)

#login page
@app.route('/login-form')
def loginForm():
    return render_template('login.html')

#login
@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        user =User.query.filter_by(email=email).filter_by(password=password).first()
        if (user):
            session['logged_in']=True
            session['email']=user.email
            session['id']=user.id
            session['name']=user.name
            session['image']=user.image
            return redirect('/profile/'+str(user.id))

        else:
            return '로그인 정보가 맞지 않음'

    else:
        return "잘못된 접근"

    app.logger.debug(request.form['email'])
    app.logger.debug(user.name)

#logout
@app.route('/logout')
def logout():
    session['logged_in']=False
    session.clear()
    return redirect(url_for('index'))

#regist contents
@app.route('/add/<int:userId>',methods=['POST'])
def add(userId):
    if request.method=='POST':
        if(session['logged_in']):
            post=Post(request.form['contents'],userId.session['id'])
            db_session.add(post)
            db_session.commit()
            return redirect('/profile/'+str(userId))
        else:
            return "로그인 해주세요"

    else:
        return '잘못된 접근'


#remove contents
@app.route('/delete/<int:userId>/<int:postId>')
def delete(userId,postId):
    if(session['logged_in']):
        Post.query.filter_by(id=postId).delete()
        return redirect('/profile/'+str (userId))
    else:
        return '잘못된 접근'