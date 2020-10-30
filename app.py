import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # sqlalchemy 갖고온다

basedir = os.path.abspath(os.path.dirname(__file__))   # 현재있는 파일의 directory name 을 절대경로로 지정해준다
dbfile = os.path.join(basedir, 'db.sqlite')   # 현재 basedir 에 db.sqlit 라는 db 파일을 생성한다
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True   # teardown 할때마다 commit 을 한다 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):    # M V C
    __tablename__ : 'test_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

db.create_all()

@app.route('/')
def hello():
    return 'Hello World!'