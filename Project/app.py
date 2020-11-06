from flask import Flask    # flask import 해주기
from api_v1 import api as api_v1


app = Flask(__name__)     # 변하지않는 1번
app.register_blueprint(api_v1, url_prefix='/api_v1')    # 뷰를 분리할때 사용하는 blueprint

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)    