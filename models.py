from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DogWalker(db.Model):
    __tablename__ = 'dogwalker'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))


    # 직렬화
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'password' : self.password,
            'userid' : self.userid,
            'username' : self.username,
        }