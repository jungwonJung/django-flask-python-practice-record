from flask import jsonify
from flask import request  # request 하기위해 import
import requests

from . import api

@api.route('/todos', methods=['GET','POST'])
def todos(): 
    if request.method == 'POST':    # 요청받은 method가 POST 일 경우
        res = requests.post('https://hooks.slack.com/services/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', json={          # incoming webhook url 카피해서 붙힘
            'text': '오늘 할일을 적어주세요!!'
        }, headers={ 'Content-Type': 'application/json'})


    elif request.method == 'GET':
        pass

    data = request.get_json()
    return jsonify(data)           # 입력받은 데이터를 그대로 반환하게 만듬  


@api.route('/tests', methods=['POST'])
def tests():
    res = request.form['text']
    print(res)
    return jsonify(res)

