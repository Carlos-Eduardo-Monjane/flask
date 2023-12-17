from flask import Flask, render_template, request, jsonify
import requests
from bardapi import SESSION_HEADERS
from bardapi import Bard


app = Flask(__name__)
token = "eQgaoLKfSx5xmduYq_HwnXYOJCB4Tr1XalQq32s-zqMJG96aeB_GqNC24JTyjrBVmG60PQ."

session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token)
session.cookies.set("__Secure-1PSIDTS","sidts-CjIBPVxjSlo377k3v2NAsN2M6g-XXbqziSbyDFGDpzHocuxX43wIGtxCP1-7q4u-tPQLKRAA")
session.cookies.set("__Secure-1PSIDCC","ABTWhQHSxdksLdP6b5Af0gLU3WMbo7ZzC5fGRTUC-8wNaM90vzmKvhNFIydZ-6aqCturZy5oQfg")



# print(bard.get_answer("quem é o presidente de brasil")['content'])

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/teste', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Olá mazza charles!'})

@app.route('/perguntar', methods=['POST'])
def post():
    data = request.get_json()
    bard = Bard(token=token, session=session)
    resposta = bard.get_answer("quem é o presidente de brasil")['content']
    return jsonify({'message': resposta})

if __name__ == '__main__':
  app.run(port=5000)

