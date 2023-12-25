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

    token = "eQgaoECt4ON9dOEL3GHfvhV-TuYRcj9959E4blRe_OljLT176rHJEWoJFHSUvPM6g4WRqg."
    
    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", token)
    session.cookies.set("__Secure-1PSIDTS","sidts-CjIBPVxjSkjDk1cgfNZCzEWbhTywKkC9hjJ5fHl-wO8971UGqjISvGhYME9ixQoexaHF8RAA")
    session.cookies.set("__Secure-1PSIDCC","ABTWhQHzzTd8hdMWi6JKRrcCd-qw7lrNFOHb4bvkLSaGXIn4OnLiGBzLo05tnKmiTuaFBMqMSkY")

    bard = Bard(token=token, session=session)


    prompt = request.json['prompt']
    # data = request.get_json()
    resposta = bard.get_answer(prompt)['content']
    return jsonify({'message': resposta})

if __name__ == '__main__':
  app.run(port=5000)

