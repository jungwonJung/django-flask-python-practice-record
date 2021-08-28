# models.py 를 만들었기때문에 기존에 만든 코드들을 복사해옴 
from flask_sqlalchemy import SQLAlchemy

# basedir = os.path.abspath(os.path.dirname(__file__))   # 현재있는 파일의 directory name 을 절대경로로 지정해준다
# dbfile = os.path.join(basedir, 'db.sqlite')  

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile 
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True   # teardown 할때마다 commit 을 한다 
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 순환구조 app 동작후 models db저장을위해 app.py 로 다시이동

db = SQLAlchemy()

class Dogwalker(db.Model):
    __tablename__ = 'dogwalker'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))