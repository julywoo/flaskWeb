#coding:utf-8
from app import app

app.secret_key='board_key'
app.config['SQLALCHEMY_ECHO']=True

if __name__=='__main__':
    app.run(host='0.0.0.0')
