#coding:utf-8

import datetime
from sqlalchemy import Column,INT,String,Text,DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from database import Base


#users table mapping
class User(Base):
    __tablename__='users'
    id=Column(INT,primary_key=True)
    name=Column(String(45),unique=False,nullable=False)
    password=Column(String(45),unique=False,nullable=False)
    email=Column(String(100),unique=True,nullable=False)
    image=Column(String(200),unique=False)

    posts=relationship('Post',backref='user',lazy='dynamic')

    def __init__(self,name=None,password=None,email=None,image=None):
        self.name=name
        self.password=password
        self.email=email
        self.image=image

#post table mapping
class Post(Base):
    __tablename__='posts'
    id=Column(INT,primary_key=True)
    contents=Column(Text,unique=False)
    userid=Column(INT,nullable=False)
    writer=Column(INT,ForeignKey('users.id'),nullable=False)
    date=Column(DateTime,default=datetime.datetime.utcnow,unique=False)
    users=relationship('User',backref='post',lazy='joined')

    def __init__(self,content=None,userid=None,writer=None):
        self.contents=content
        self.userid=userid
        self.writer=writer


