import os
from flask import Flask
from flask import redirect
from flask import render_template  #template 연결 
from flask import request    # 플라스크 get,post 위해 request 갖고오기
from models import db  
from models import Dogwalker    # moels.py 안에서 만든 class 가져오기 
from flask_wtf.csrf import CSRFProtect # csrf 설정추가
from forms import RegisterForm
# from flask_sqlalchemy import SQLAlchemy # sqlalchemy 갖고온다

# basedir = os.path.abspath(os.path.dirname(__file__))   # 현재있는 파일의 directory name 을 절대경로로 지정해준다
# dbfile = os.path.join(basedir, 'db.sqlite')   # 현재 basedir 에 db.sqlit 라는 db 파일을 생성한다
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile 
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True   # teardown 할때마다 commit 을 한다 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)   models.py 로 이동
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
    # if request.method == 'POST':
    #     # 회원정보 생성
    #     userid = request.form.get('userid')
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     re_password = request.form.get('re-password')     23번 코드 추가함으로써 삭제가능

        # if (userid and username and password and re_password) and password == re_password:   # 이중에 하나라도 없으면 register.html 로 render 해버린다,23번코드 추가 forms 에서 equalto 설정  
        
        dogwalker = Dogwalker()

        # dogwalker.userid = userid
        # dogwalker.username = username
        # dogwalker.password = password   form 기능을 사용하면서 data 를 가져오기위해 36~38 코드처럼 수정

        dogwalker.userid = form.data.get('userid')
        dogwalker.username = form.data.get('username')
        dogwalker.password = form.data.get('password')

        db.session.add(dogwalker)    #  19번부터 모든 값이 제대로 동작한경우에 DataBase 에 저장된다 
        db.session.commit()
        print('Success!')            # 정상적으로 동작하는지 확인하기위해 추가

        return redirect('/')   # 사용하기위해  3번 코드추가
    return render_template('register.html', form=form)  # 함수의 인자값을 전달할때처럼 작성

@app.route('/')
def hello():
    return render_template('hello.html')  #hello.html 이라는 파일로 연결  templates 라는 폴더에 바로연결

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))  
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile 
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'asdasdkdmvkmsdflkgjaeklasd'  # csrf 설정추가

    csrf = CSRFProtect()   # csrf 설정추가
    csrf.init_app(app)
    db.init_app(app)     # 24~26 config 설정하는 명령어가 굉장히 많지만 그걸 초기화시키는코드
    db.app = app     # app 을 명시적으로 입력가능
    db.create_all()
    app.run(host='127.0.0.1', port=5000, debug=True)   # 기존의 flask 명령어 말고 파이썬명령어로 실행가능하게 개선