import os
from flask import Flask
from flask_jwt import JWT   # pip install Flask-JWT 후 import 해주기
from flask import render_template 
from api_v1 import api as api_v1 
from models import db, DogWalker

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix='/api/v1')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/')
def home():
    return render_template('home.html')

#db 가져오기 
basedir = os.path.abspath(os.path.dirname(__file__))  
dbfile = os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'asdasdkdmvkmsdflkgjaeklasd'  
  
db.init_app(app)    
db.app = app     
db.create_all()        


def authenticate(username, password):
    user = DogWalker.query.filter(DogWalker.userid == username).first()   # DogWalker 전체를 가져오고나서 DogWalker의 userid 가 일치할때
    if user.password == password:
        return user

def identity(payload):
    userid = payload['identity']
    return DogWalker.query.filter(DogWalker.userid == userid).first()

jwt = JWT(app, authenticate)

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000, debug=True)   