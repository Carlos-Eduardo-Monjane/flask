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

    token = "egiJeZdXNq_NgIfYUAIGSzVlwYu3VCQqfIcZ225Efmcuqbh84aAnqWbGJ0ECgxaUYnui5w."
    
    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", token)
    session.cookies.set("__Secure-1PSIDTS","sidts-CjEBPVxjSnI2lvyJgBm2cnYc08RKIkFoMQGmwO2UKvnU4-GvwMFxF0RAztsInS3_bMsSEAA")
    session.cookies.set("__Secure-1PSIDCC","ABTWhQGbzNSx-CAjLG-l1JSh7_hV8tNjs8XAmCbjr6jUtkxMy-6Hka5tnxoOrGOnSzkdNTvZ")

    bard = Bard(token=token, session=session)


    prompt = request.json['prompt']
    # data = request.get_json()
    resposta = bard.get_answer(prompt)['content']
    return jsonify({'message': resposta})

if __name__ == '__main__':
  app.run(port=5000)

