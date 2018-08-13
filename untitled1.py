from flask import Flask, json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/mybatislog/rawLog', methods=['POST','GET'])
def hello_world2():
    return json.dumps({"success":True})


@app.route('/mybatispaidinfo/validateNew', methods=['POST','GET'])
def hello_world3():
    return json.dumps({"valid":True,"validTo":1850236326000})


if __name__ == '__main__':
    app.run(port=80)
