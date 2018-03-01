from flask_api import FlaskAPI
from flask import request

# from backends.big_query import BqClient
app = FlaskAPI(__name__)
# os.environ.setdefault('FLASK_APP', 'main.py')
# os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', 'backends/credentials.json')


@app.route('/')
def hello():
    print("asd")
    return 'Aplicativo Flask pub-sub'


@app.route("/pub-sub/", methods=['POST'])
def pob_sub():
    print(request.data)
    if request.data.get("message"):
        print(request.data.get("message"))
    return request.data, 200


if __name__ == '__main__':
    app.run(debug=True)
