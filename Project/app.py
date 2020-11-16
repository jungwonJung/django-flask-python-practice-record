import os
from flask import request
from flask import Flask    # flask import 해주기
from models import db
from api_v1 import api as api_v1


app = Flask(__name__)     # 변하지않는 1번
app.register_blueprint(api_v1, url_prefix='/api_v1')    # 뷰를 분리할때 사용하는 blueprint

basedir = os.path.abspath(os.path.dirname(__file__))   # base dir 가져오기
dbfile = os.path.join(basedir, 'db.sqlite')       # db 는 basedir 에 sqlite 사용

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'slasudhaiusdhiuasnuiansuidn'

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)    