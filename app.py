import os
from flask import Flask
from flask import render_template  #template 연결 
from models import db
# from flask_sqlalchemy import SQLAlchemy # sqlalchemy 갖고온다

# basedir = os.path.abspath(os.path.dirname(__file__))   # 현재있는 파일의 directory name 을 절대경로로 지정해준다
# dbfile = os.path.join(basedir, 'db.sqlite')   # 현재 basedir 에 db.sqlit 라는 db 파일을 생성한다
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile 
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True   # teardown 할때마다 commit 을 한다 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)   models.py 로 이동

@app.route('/')
def hello():
    return render_template('hello.html')  #hello.html 이라는 파일로 연결  templates 라는 폴더에 바로연결

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))  
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile 
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)     # 24~26 config 설정하는 명령어가 굉장히 많지만 그걸 초기화시키는코드
    db.app = app     # app 을 명시적으로 입력가능
    db.create_all()
    app.run(host='127.0.0.1', port=5000, debug=True)   # 기존의 flask 명령어 말고 파이썬명령어로 실행가능하게 개선