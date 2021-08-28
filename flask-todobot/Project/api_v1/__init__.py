from flask import Blueprint  # flask 안에 있는 Blueprint 를 가져온다
          

api = Blueprint('api', __name__)

from . import todo # 현재폴더 안에 있는 todo 가져오기   api 아래에 todo를 가져와야 엉키지않음