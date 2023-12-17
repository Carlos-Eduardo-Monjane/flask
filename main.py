from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/teste', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Olá mazza charles!'})

@app.route('/perguntar', methods=['POST'])
def post():
    import requests
    from bardapi import SESSION_HEADERS
    from bardapi import Bard

    token = "eQgaoLKfSx5xmduYq_HwnXYOJCB4Tr1XalQq32s-zqMJG96aeB_GqNC24JTyjrBVmG60PQ."
    
    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", token)
    session.cookies.set("__Secure-1PSIDTS","sidts-CjIBPVxjSiiLe8A1mzGv2uC9ZDhnByUiIkBQi36UUGhvs7eDxWrOZNllmpbCTr6lPOdX5xAA")
    session.cookies.set("__Secure-1PSIDCC","ABTWhQHYqWkZT6h4Mme1OM-vLq1LioS6ldP6Q3wvvG8DOGTXlrl2Fkk2zmx4BZwLxDSkPBrv4-c")

    bard = Bard(token=token, session=session)


    prompt = request.json['prompt']
    # data = request.get_json()
    resposta = bard.get_answer(prompt)['content']
    return jsonify({'message': resposta})

if __name__ == '__main__':
  app.run(port=5000)

