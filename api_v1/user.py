from flask import jsonify
from . import api
from flask import request  # 폼을 사용하지않기때문에 request 를 가져온다
from models import DogWalker, db
from flask_jwt import jwt_required   # 데코레이터 사용



@api.route('/users', methods=['GET','POST'])
@jwt_required()   # 로그인을 하지않고 home 으로 갈시 에러가뜸
def users():
    if request.method == 'POST':        # 만약요청이 POST 일 경우
        data = request.get_json()           # data를 json 형태로 가져오겟다고 함수선언
        userid = data.get('userid')      # form 이 아니라 json 형태의 데이터로 받아오기때문에
        username = data.get('username')
        password = data.get('password')
        re_password = data.get('re-password')

        if not (userid and username and password and re_password):
            return jsonify({'error' : 'No arguments'}), 400  # 에러메시지와 함께 400 에러 발생시키겠음


        if password != re_password:
            return jsonify({'error' : 'Wrong match password'}), 400

        dogwalker = DogWalker()
        dogwalker.userid = userid
        dogwalker.username = username
        dogwalker.password = password

        db.session.add(dogwalker)   
        db.session.commit()

        return jsonify(), 201    # 아무이상없이 동작하게되는경우 201이라는 코드를 출력  

    users = DogWalker.query.all()    # 모든데이터를 가져오는 코드
    return jsonify([user.serialize for user in users ])

# @api.route('/users/login', methods=['GET'])
# def login():
#     if request.method == 'GET'
#     data = request.get_json()
#     userid = data.get('userid')
#     password = data.get('password')

#     if not (userid and   password ):
#             return jsonify({'error' : 'No arguments'}), 400  # 에러메시지와 함께 400 에러 발생시키겠음

#         dogwalker = DogWalker()
#         dogwalker.userid = userid
#         dogwalker.username = username
#         dogwalker.password = password

#         db.session.add(dogwalker)   
#         db.session.commit()

#         return jsonify(), 201

@api.route('/users/<uid>', methods=['GET', 'PUT', 'DELETE'])   # URL 에서 입력값을 받을수있게 <uid> 로 표현 수정 삭제 조회를 지원하기위해 'GET', 'PUT', 'DELETE' 작성
def user_detail(uid):
    if request.method == 'GET':         #  조회 요청을받으면 
        user = DogWalker.query.filter(DogWalker.id == uid).first()    # 도그워커의 id 값이 입력받은 uid 랑 같은애를 first를 사용 하나만 뽑아낸다
        return jsonify(user.serialize)   # user 는 클래스 변수이므로 serialize 해야함\

    elif request.method == 'DELETE':
        DogWalker.query.delete(DogWalker.id == uid)    # 입력받은 uid 를 삭제해준다 그러고나서 아무값도 반환하지않는다
        return jsonify(), 204                          # 그냥성공하고 아무것도 표시안해줄때는 200, 204는 None contents
    
    # PUT 은 전체를 replace 하듯이 전체를 수정하고 PATCH 는 일부분만 수정한다 구현하기따라 다름 반대일수도있음 

    data = request.get_json()


    userid = data.get('userid')
    username = data.get('username')
    password = data.get('password')

    updated_data = {}    # 값이 없으면 안넣기위해 빈값을 넣는다 
    if userid:
        updated_data['userid'] = userid         # 업데이트되는 데이터에 userid 가 있으면 채워넣고
    if username:
        updated_data['username'] = username      # 업데이트되는 데이터에 username 가 있으면 채워넣고
    if password:
        updated_data['password'] = password     # 업데이트되는 데이터에 password 가 있으면 채워넣고

    DogWalker.query.filter(DogWalker.id == uid).update(updated_data)   # 정상적으로 업데이트를하고
    user = DogWalker.query.filter(DogWalker.id == uid).first()    # 사용자정보를 다시 가지고오고나서  보여준다
    return jsonify(user.serialize)   